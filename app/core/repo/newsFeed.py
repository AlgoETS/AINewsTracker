# -*- coding: utf-8 -*-
# database_operations.py
from bson import ObjectId
from database import collection_rss_feeds

from app.models.newsFeed import NewsFeed


def create_rss_feed(rss_feed: NewsFeed):
    rss_feed_dict = rss_feed.dict()
    rss_feed_dict["_id"] = str(ObjectId())  # Convert ObjectId to a string
    result = collection_rss_feeds.insert_one(rss_feed_dict)
    return result.inserted_id


def get_rss_feed_by_id(rss_feed_id: str) -> NewsFeed:
    rss_feed = collection_rss_feeds.find_one({"_id": rss_feed_id})
    return NewsFeed(**rss_feed)


def update_rss_feed(rss_feed_id: str, updated_rss_feed: NewsFeed):
    updated_rss_feed_dict = updated_rss_feed.dict()
    collection_rss_feeds.update_one(
        {"_id": rss_feed_id}, {"$set": updated_rss_feed_dict}
    )


def delete_rss_feed(rss_feed_id: str):
    collection_rss_feeds.delete_one({"_id": rss_feed_id})
