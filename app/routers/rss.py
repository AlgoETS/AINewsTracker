from fastapi import APIRouter
from pydantic import BaseModel
from bson import ObjectId
from ..core.services.rss.source import Source
from ..core.services.rss.rss import RSSFeed

router = APIRouter(
    prefix="/rss",
    tags=["rss"],
    responses={404: {"description": "Not found"}},
)
rss_feed = RSSFeed()


@router.post("/rss/feed")
def fetch_rss_feed(source: str , limit: int):
    # get source from name
    source = Source(source)
    entries = rss_feed.fetch_feed_entries(source.url, limit)
    rss_items = []
    for entry in entries:
        rss_item = RSSFeed()
        rss_items.append(rss_item)
    return rss_items