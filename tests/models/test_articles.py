import pytest
from datetime import datetime
from app.models import Article, Score

def test_article_model():
    """Test the Article model"""
    article = Article(
        id="1",
        title="Test Title",
        content="Test Content",
        url="https://testurl.com",
        date=datetime.now(),
    )

    assert article.id == "1"
    assert article.title == "Test Title"
    assert article.content == "Test Content"
    assert article.url == "https://testurl.com"
    assert isinstance(article.date, datetime)
    assert article.score_id is None
    assert article.company_id is None


def test_score_model():
    """Test the Score model"""
    score = Score(
        id="1",
        sentiment_score=0.75,
        sentiment="positive",
        article_id="1",
    )

    assert score.id == "1"
    assert score.sentiment_score == 0.75
    assert score.sentiment == "positive"
    assert score.article_id == "1"


# Run tests with: pytest -v
