# -*- coding: utf-8 -*-
from datetime import datetime

from app.models import Article


def test_article_model():
    """Test the Article model"""
    article = Article(
        id="1",
        title="Test Title",
        content="Test Content",
        url="https://testurl.com",
        date=datetime.now(),
        author="Test Author",
        likes="100",
        comments="100",
        source="Test Source",
        sentiment_score=0.5,
        sentiment="Positive",
        tickers=["AAPL", "TSLA"],
        company_id=1,
    )

    assert article.id == "1"
    assert article.title == "Test Title"
    assert article.content == "Test Content"
    assert article.url == "https://testurl.com"
    assert isinstance(article.date, datetime)
    assert article.author == "Test Author"
    assert article.likes == 100
    assert article.source == "Test Source"
    assert article.sentiment_score == 0.5
    assert article.sentiment == "Positive"
    assert article.tickers == ["AAPL", "TSLA"]
    assert article.company_id == "1"


# Run tests with: pytest -v
