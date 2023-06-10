import pytest
from datetime import datetime
from app.models import NewsFeed

def test_newsfeed_model():
    """Test the NewsFeed model"""
    newsfeed = NewsFeed(
        id="1",
        link="https://newsfeed.example.com",
        data={"articles": ["article1", "article2"]},
        number_of_articles=2,
        last_fetch=datetime.now(),
        last_update=datetime.now(),
        last_article=datetime.now(),
    )

    assert newsfeed.id == "1"
    assert newsfeed.link == "https://newsfeed.example.com"
    assert newsfeed.data == {"articles": ["article1", "article2"]}
    assert newsfeed.number_of_articles == 2
    assert isinstance(newsfeed.last_fetch, datetime)
    assert isinstance(newsfeed.last_update, datetime)
    assert isinstance(newsfeed.last_article, datetime)
