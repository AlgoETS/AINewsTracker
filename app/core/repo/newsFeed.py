# database_operations.py
from database import collection_rss_feeds
from app.models import newsFeed
from bson import ObjectId

def create_rss_feed(rss_feed: newsFeed):
    rss_feed_dict = rss_feed.dict()
    rss_feed_dict["_id"] = str(ObjectId())  # Convert ObjectId to a string
    result = collection_rss_feeds.insert_one(rss_feed_dict)
    return result.inserted_id

def get_rss_feed_by_id(rss_feed_id: str) -> newsFeed:
    rss_feed = collection_rss_feeds.find_one({"_id": rss_feed_id})
    return newsFeed(**rss_feed)

def update_rss_feed(rss_feed_id: str, updated_rss_feed: newsFeed):
    updated_rss_feed_dict = updated_rss_feed.dict()
    collection_rss_feeds.update_one({"_id": rss_feed_id}, {"$set": updated_rss_feed_dict})

def delete_rss_feed(rss_feed_id: str):
    collection_rss_feeds.delete_one({"_id": rss_feed_id})
