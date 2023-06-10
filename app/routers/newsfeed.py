# rss_feed_routes.py
from fastapi import APIRouter
from .models import RSSFeed
from core import create_rss_feed, get_rss_feed_by_id, update_rss_feed, delete_rss_feed

router = APIRouter()

@router.post("/", response_model=RSSFeed)
async def create_feed(rss_feed: RSSFeed):
    feed_id = create_rss_feed(rss_feed)
    return {**rss_feed.dict(), "_id": feed_id}

@router.get("/{rss_feed_id}", response_model=RSSFeed)
async def read_feed(rss_feed_id: str):
    return get_rss_feed_by_id(rss_feed_id)

@router.put("/{rss_feed_id}", response_model=RSSFeed)
async def update_feed(rss_feed_id: str, rss_feed: RSSFeed):
    update_rss_feed(rss_feed_id, rss_feed)
    return {**rss_feed.dict(), "_id": rss_feed_id}

@router.delete("/{rss_feed_id}")
async def delete_feed(rss_feed_id: str):
    delete_rss_feed(rss_feed_id)
    return {"message": f"RSS Feed {rss_feed_id} has been deleted."}
