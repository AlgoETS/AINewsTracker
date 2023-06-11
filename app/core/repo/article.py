# -*- coding: utf-8 -*-
from typing import Optional

from bson.objectid import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient

from app.core.database import MongoDB
from app.models.article import Article

client = AsyncIOMotorClient()
db = client.AINewsTracker
collection = db.articles  # use your collection name here

async def create_article(article: Article):
    article_dict = article.dict()
    article_dict["_id"] = str(ObjectId())  # Convert ObjectId to a string
    result = await collection.insert_one(article_dict)
    return result.inserted_id

async def create_articles(articles: list[Article]):
    article_dicts = [article.dict() for article in articles]
    for article_dict in article_dicts:
        article_dict["_id"] = str(ObjectId())  # Convert ObjectId to a string
    result = await collection.insert_many(article_dicts)
    return result.inserted_ids

async def get_all_articles() -> list[Article]:
    cursor = collection.find()
    articles = await cursor.to_list(length=100)  # specify max limit here
    return [Article(**article) for article in articles]

async def get_article_by_id(article_id: str) -> Optional[Article]:
    article = await collection.find_one({"_id": article_id})
    return Article(**article) if article else None

async def get_articles_by_company_id(company_id: str) -> list[Article]:
    cursor = collection.find({"company_id": company_id})
    articles = await cursor.to_list(length=100)  # specify max limit here
    return [Article(**article) for article in articles]

async def get_score_by_article_id(article_id: str) -> int:
    article = await collection.find_one({"article_id": article_id})
    if article is not None:
        score = article.get("score")
        if score is not None:
            return int(score)
    return None

async def delete_article_by_id(article_id: str):
    result = await collection.delete_one({"_id": article_id})
    return result.deleted_count
