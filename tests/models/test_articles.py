# -*- coding: utf-8 -*-
from datetime import datetime

from app.models import Article

def test_article_model():
    """Test the Article model"""
    article = Article(
        title="Test Title",
        url="https://testurl.com",
        publishedDate="2023-06-28T00:00:00",
        text="Test Content",
        source_name="Test Source",
        author="Test Author",
        likes="100",
        comments="100",
        sentiment_score=0.5,
        sentiment="Positive",
        tickers=["AAPL", "TSLA"],
        company_id=1,
    )

    assert article.title == "Test Title"
    assert article.text == "Test Content"
    assert article.url == "https://testurl.com"
    assert article.publishedDate == "2023-06-28T00:00:00"
    assert article.author == "Test Author"
    assert article.likes == 100
    assert article.source_name == "Test Source"
    assert article.sentiment_score == 0.5
    assert article.sentiment == "Positive"
    assert article.tickers == ["AAPL", "TSLA"]
    assert article.company_id == "1"
