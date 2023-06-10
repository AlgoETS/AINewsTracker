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
    score_id: Optional[str] = None
    company_id: Optional[str] = None


class Score(BaseModel):
    id: Optional[str]
    sentiment_score: float
    sentiment: str
    article_id: str
