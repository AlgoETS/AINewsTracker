from fastapi import APIRouter
from pydantic import BaseModel
from bson import ObjectId
from ..services.source import Source
from .database import collection_companies
from rss_feed import RSSFeed

router = APIRouter()
rss_feed = RSSFeed()


@router.post("/rss/feed")
def fetch_rss_feed(source: Source, limit: int):
    entries = rss_feed.fetch_feed_entries(source.url, limit)
    rss_items = []
    for entry in entries:
        rss_item = RSSFeed()
        rss_items.append(rss_item)
    return rss_items