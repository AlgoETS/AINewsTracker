# -*- coding: utf-8 -*-
from typing import Optional

from bson.objectid import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient

from app.core.database import MongoDB
from app.models.newsFeed import NewsFeed

client = AsyncIOMotorClient()
db = client.AINewsTracker
collection = db.newsFeeds

async def create_newsFeed(newsFeed_item: NewsFeed):
    newsFeed_dict = newsFeed_item.dict()
    newsFeed_dict["_id"] = str(ObjectId())
    result = await collection.insert_one(newsFeed_dict)
    return result.inserted_id

async def create_newsFeeds(newsFeeds: list[NewsFeed]):
    newsFeed_dicts = [newsFeed_item.dict() for newsFeed_item in newsFeeds]
    for newsFeed_dict in newsFeed_dicts:
        newsFeed_dict["_id"] = str(ObjectId())
    result = await collection.insert_many(newsFeed_dicts)
    return result.inserted_ids

async def get_all_newsFeeds() -> list[NewsFeed]:
    cursor = collection.find()
    newsFeeds = await cursor.to_list(length=100)  # specify max limit here
    return [NewsFeed(**newsFeed_item) for newsFeed_item in newsFeeds]

async def get_newsFeed_by_id(newsFeed_id: str) -> Optional[NewsFeed]:
    newsFeed_item = await collection.find_one({"_id": newsFeed_id})
    return NewsFeed(**newsFeed_item) if newsFeed_item else None

async def delete_newsFeed_by_id(newsFeed_id: str):
    result = await collection.delete_one({"_id": newsFeed_id})
    return result.deleted_count

async def update_newsFeed_by_id(newsFeed_id: str, newsFeed_item: NewsFeed):
    result = await collection.replace_one({"_id": newsFeed_id}, newsFeed_item.dict())
    return result.modified_count

