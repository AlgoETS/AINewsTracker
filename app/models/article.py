# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Article(BaseModel):
    id: Optional[str]
    title: str
    content: str
    url: str
    date: datetime
    author: str
    likes: int
    comments: int
    source: str
    sentiment_score: float
    sentiment: str
    tickers: list[str] = []
    company_id: Optional[str] = None

class Comment(BaseModel):
    id: Optional[str]
    article_id: str
    content: str
    date: datetime
