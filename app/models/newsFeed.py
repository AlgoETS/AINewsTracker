# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class NewsFeed(BaseModel):
    id: Optional[str]
    link: str
    data: dict
    number_of_articles: int
    sector: str
    country: str
    language: str
    type: str
    last_fetch: datetime
    last_update: datetime
    last_article: datetime
