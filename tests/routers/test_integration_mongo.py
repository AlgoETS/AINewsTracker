import os
from datetime import datetime, timezone
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient
from pymongo import MongoClient

from app.core.database.db import MongoDB, settings as database_settings
from app.main import app
from app.routers import integration


@pytest.mark.integration
def test_article_feed_reads_from_mongodb(monkeypatch):
    mongodb_url = os.getenv("AINEWSTRACKER_TEST_MONGODB_URL")
    if not mongodb_url:
        pytest.skip("AINEWSTRACKER_TEST_MONGODB_URL is not configured")

    article_id = f"integration-{uuid4()}"
    token = "integration-test-token"
    collection = MongoClient(mongodb_url, tz_aware=True)["AINewsTracker"]["articles"]
    collection.insert_one(
        {
            "article_id": article_id,
            "title": "Integration article",
            "url": f"https://publisher.example/{article_id}",
            "publishedDate": "2026-10-15 14:30:00",
            "published_at": datetime(2026, 10, 15, 14, 30, tzinfo=timezone.utc),
            "ingested_at": datetime(2026, 10, 15, 14, 31, tzinfo=timezone.utc),
            "text": "This text must not leave the integration feed.",
            "source_name": "publisher.example",
            "sentiment_score": 0.8,
            "sentiment": "positive",
            "sentiment_probabilities": {"positive": 0.8, "negative": 0.1, "neutral": 0.1},
            "model_name": "ProsusAI/finbert",
            "model_version": "test",
            "author": None,
            "likes": None,
            "comments": None,
            "tickers": ["AAPL"],
        }
    )

    MongoDB._instance = None
    monkeypatch.setattr(database_settings, "MONGODB_URL", mongodb_url)
    monkeypatch.setattr(integration.settings, "AINEWSTRACKER_SERVICE_TOKEN", token)

    try:
        with TestClient(app) as client:
            response = client.get(
                "/v1/articles?symbols=AAPL&limit=1",
                headers={"Authorization": f"Bearer {token}"},
            )
    finally:
        MongoDB().close()
        collection.delete_one({"article_id": article_id})

    assert response.status_code == 200
    article = response.json()["data"][0]
    assert article["articleId"] == article_id
    assert article["publishedAt"] == "2026-10-15T14:30:00+00:00"
    assert "text" not in article