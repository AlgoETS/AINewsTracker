from datetime import datetime, timezone

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.models.article import Article
from app.routers import integration
from app.routers.integration import decode_cursor, encode_cursor, serialize_article


def integration_article() -> Article:
    return Article(
        article_id="fmp_example",
        title="Example article",
        url="https://publisher.example/article",
        publishedDate="2026-10-02 12:31:18",
        published_at=datetime(2026, 10, 2, 12, 31, 18, tzinfo=timezone.utc),
        ingested_at=datetime(2026, 10, 2, 12, 32, tzinfo=timezone.utc),
        text="Not included in the integration response",
        source_name="publisher.example",
        sentiment_score=0.7,
        sentiment="positive",
        sentiment_probabilities={"positive": 0.7, "negative": 0.1, "neutral": 0.2},
        model_name="ProsusAI/finbert",
        model_version="revision",
        tickers=["AAPL"],
    )


def test_cursor_round_trip_preserves_article_ordering_fields():
    article = integration_article()

    published_at, article_id = decode_cursor(encode_cursor(article))

    assert published_at == article.published_at
    assert article_id == article.article_id


def test_serialize_article_excludes_raw_text():
    serialized = serialize_article(integration_article())

    assert serialized["articleId"] == "fmp_example"
    assert serialized["sentimentProbabilities"]["positive"] == 0.7
    assert "text" not in serialized


def test_decode_cursor_rejects_invalid_value():
    with pytest.raises(ValueError, match="invalid cursor"):
        decode_cursor("not-a-cursor")


def test_article_feed_requires_service_credential_and_returns_next_cursor(monkeypatch):
    first_article = integration_article()
    second_article = integration_article().copy(update={"article_id": "fmp_next"})

    async def get_articles(*args, **kwargs):
        return [first_article, second_article]

    monkeypatch.setattr(integration, "get_articles_for_integration", get_articles)
    monkeypatch.setattr(integration.settings, "AINEWSTRACKER_SERVICE_TOKEN", "test-token")
    client = TestClient(app)

    unauthorized = client.get("/v1/articles")
    response = client.get(
        "/v1/articles?symbols=aapl&from=2026-10-02T00:00:00Z&to=2026-10-03T00:00:00Z&limit=1",
        headers={"Authorization": "Bearer test-token"},
    )

    assert unauthorized.status_code == 401
    assert response.status_code == 200
    assert response.json()["data"][0]["articleId"] == "fmp_example"
    assert "text" not in response.json()["data"][0]
    assert response.json()["meta"]["nextCursor"] is not None