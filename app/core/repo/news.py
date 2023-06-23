from typing import Optional
from bson.objectid import ObjectId

from app.core.database import MongoDB
from app.models.news import News

# Initialize MongoDB connection
mongo_db = MongoDB()
collection = mongo_db.get_collection("news")

async def create_news(news_item: News):
    news_dict = news_item.dict()
    news_dict["_id"] = str(ObjectId())
    return await collection.insert_one(news_dict)

async def create_news_items(news_items: list[News]):
    news_items = [dict(item.dict(), _id=str(ObjectId())) for item in news_items]
    return await collection.insert_many(news_items)

async def get_all_news_items() -> list[News]:
    news_items = await collection.find().to_list(length=100)  # specify max limit here
    return [News(**news_item) for news_item in news_items]

async def get_news_by_id(news_id: str) -> Optional[News]:
    news_item = await collection.find_one({"_id": news_id})
    return News(**news_item) if news_item else None

async def get_news_by_name(news_name: str) -> Optional[News]:
    news_item = await collection.find_one({"name": news_name})
    return News(**news_item) if news_item else None

async def delete_news_by_id(news_id: str):
    return await collection.delete_one({"_id": news_id})

async def update_news_by_id(news_id: str, news_item: News):
    return await collection.replace_one({"_id": news_id}, news_item.dict(exclude_unset=True))