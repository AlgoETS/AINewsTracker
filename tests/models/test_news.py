# -*- coding: utf-8 -*-
from datetime import datetime

from pydantic import BaseModel
from typing import List, Optional

from app.models.news import News

def test_news_model():
    """Test the News model"""
    some_datetime = datetime(2022, 1, 1)  # or any other fixed datetime
    news = News(
        source_name="Example News Source",
        topics=["finance"],
        country="US",
        language="English",
        type="news",
        source_url="https://example.com",
        id="1",
        link="https://news.example.com",
        data={"articles": ["article1", "article2"]},
        number_of_articles=2,
        last_fetch=some_datetime,
        last_update=some_datetime,
        last_article=some_datetime,
    )

    assert news.source_name == "Example News Source"
    assert news.topics == ["finance"]
    assert news.country == "US"
    assert news.language == "English"
    assert news.type == "news"
    assert news.source_url == "https://example.com"
    assert news.id == "1"
    assert news.link == "https://news.example.com"
    assert news.data == {"articles": ["article1", "article2"]}
    assert news.number_of_articles == 2
    assert news.last_fetch == some_datetime
    assert news.last_update == some_datetime
    assert news.last_article == some_datetime
