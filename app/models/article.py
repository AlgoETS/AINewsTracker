# -*- coding: utf-8 -*-
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class Article(BaseModel):
    title: str
    url: str
    publishedDate: str
    text: str
    source_name: str
    sentiment_score: float
    sentiment: str
    author: Optional[str]
    likes: Optional[int]
    comments: Optional[int]
    tickers: Optional[list[str]] = []
    company_id: Optional[str] = None
    topics: Optional[List[str]] = None
    summary: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True

class Comment(BaseModel):
    id: Optional[str]
    article_id: str
    content: str
    date: datetime

    class Config:
        arbitrary_types_allowed = True
