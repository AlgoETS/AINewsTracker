from pydantic import BaseModel
from datetime import datetime

class RSSFeed(BaseModel):
    link: str
    data: dict
    last_fetch: datetime
