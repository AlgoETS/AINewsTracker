from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class NewsFeed(BaseModel):
    id: Optional[str]
    link: str
    data: dict
    number_of_articles: int
    last_fetch: datetime
    last_update: datetime
    last_article: datetime
