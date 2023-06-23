from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class News(BaseModel):
    source_name: str
    topics: List[str] = []
    country: str
    language: str
    type: str
    source_url: str
    id: Optional[str]
    link: str
    data: dict
    number_of_articles: int
    last_fetch: datetime
    last_update: datetime
    last_article: datetime

    class Config:
        arbitrary_types_allowed = True
