# -*- coding: utf-8 -*-
from datetime import datetime

from app.models import NewsFeed


def test_newsfeed_model():
    """Test the NewsFeed model"""
    some_datetime = datetime(2022, 1, 1)  # or any other fixed datetime
    newsfeed = NewsFeed(
        id="1",
        link="https://newsfeed.example.com",
        data={"articles": ["article1", "article2"]},
        number_of_articles=2,
        sector="finance",
        country="US",
        language="English",
        type="news",
        last_fetch=some_datetime,
        last_update=some_datetime,
        last_article=some_datetime,
    )

    assert newsfeed.id == "1"
    assert newsfeed.link == "https://newsfeed.example.com"
    assert newsfeed.data == {"articles": ["article1", "article2"]}
    assert newsfeed.number_of_articles == 2
    assert newsfeed.sector == "finance"
    assert newsfeed.country == "US"
    assert newsfeed.language == "English"
    assert newsfeed.type == "news"
    assert newsfeed.last_fetch == some_datetime
    assert newsfeed.last_update == some_datetime
    assert newsfeed.last_article == some_datetime

