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
    author: Optional[str]
    likes: Optional[int]
    comments: Optional[int]
    source: Optional[str]
    sentiment_score: float
    sentiment: str
    tickers: Optional[list[str]] = []
    company_id: Optional[str] = None
    topic: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True

class Comment(BaseModel):
    id: Optional[str]
    article_id: str
    content: str
    date: datetime

    class Config:
        arbitrary_types_allowed = True
