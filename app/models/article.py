# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Dict, List, Optional

from pydantic import BaseModel


class Article(BaseModel):
    article_id: Optional[str] = None
    title: str
    url: str
    publishedDate: str
    published_at: Optional[datetime] = None
    ingested_at: Optional[datetime] = None
    text: str
    source_name: str
    sentiment_score: float
    sentiment: str
    sentiment_probabilities: Optional[Dict[str, float]] = None
    model_name: Optional[str] = None
    model_version: Optional[str] = None
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
