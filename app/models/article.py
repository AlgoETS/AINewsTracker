from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Article(BaseModel):
    title: str
    content: str
    url: str
    date: datetime
    score_id: Optional[str] = None
    company_id: Optional[str] = None
