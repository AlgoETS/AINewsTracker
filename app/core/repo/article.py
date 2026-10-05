import logging
from datetime import datetime
from typing import List, Optional
from app.core.database.db import MongoDB
from app.models.article import Article
from bson.objectid import ObjectId
from typing import Optional, List
from app.core.logging import Logger

logger = Logger(logging.INFO).get_logger()

# Initialize MongoDB connection
mongo_db = MongoDB()
collection = mongo_db.get_collection("articles")

async def create_article(articles: List[Article]):
    news = [dict(item.dict()) for item in articles]
    inserted_ids = []
    for news_item in news:
        filter_query = {"url": news_item["url"]}  # filter condition for the upsert
        update_query = {"$set": news_item}  # update operation

        # upsert operation
        result = await collection.update_one(filter_query, update_query, upsert=True)

        # If a new document was inserted, retrieve the inserted ID
        if result.upserted_id:
            inserted_ids.append(result.upserted_id)

    return inserted_ids


async def get_all_articles() -> List[Article]:
    articles = await collection.find().to_list(length=100)
    logger.info("Articles fetched successfully")
    return [Article(**article) for article in articles]


async def get_articles_for_integration(
    symbols: List[str],
    from_time: Optional[datetime],
    to_time: Optional[datetime],
    cursor_published_at: Optional[datetime],
    cursor_article_id: Optional[str],
    limit: int,
) -> List[Article]:
    filters = [
        {"article_id": {"$exists": True, "$ne": None}},
        {"published_at": {"$exists": True, "$ne": None}},
        {"ingested_at": {"$exists": True, "$ne": None}},
        {"sentiment_probabilities": {"$exists": True, "$ne": None}},
    ]
    if symbols:
        filters.append({"tickers": {"$in": symbols}})
    if from_time is not None:
        filters.append({"published_at": {"$gte": from_time}})
    if to_time is not None:
        filters.append({"published_at": {"$lt": to_time}})
    if cursor_published_at is not None and cursor_article_id is not None:
        filters.append(
            {
                "$or": [
                    {"published_at": {"$gt": cursor_published_at}},
                    {
                        "published_at": cursor_published_at,
                        "article_id": {"$gt": cursor_article_id},
                    },
                ]
            }
        )

    cursor = collection.find({"$and": filters}).sort(
        [("published_at", 1), ("article_id", 1)]
    )
    articles = await cursor.to_list(length=limit + 1)
    return [Article(**article) for article in articles]

async def get_article_by_id(article_id: str) -> Optional[Article]:
    article = await collection.find_one({"_id": article_id})
    logger.info(f"Article {article_id} fetched successfully")
    return Article(**article) if article else None

async def get_articles_by_company_id(company_id: str) -> list[Article]:
    articles = await collection.find({"company_id": company_id}).to_list(length=100)
    logger.info(f"Articles for company {company_id} fetched successfully")
    return [Article(**article) for article in articles]

async def get_articles_by_company_ids(company_id: List[str]) -> list[Article]:
    articles = await collection.find({"company_id": {"$in": company_id}}).to_list(length=100)
    logger.info(f"Articles for companies {company_id} fetched successfully")
    return [Article(**article) for article in articles]

async def get_score_by_article_id(article_id: str) -> int:
    article = await collection.find_one({"article_id": article_id}, {"score": 1})
    logger.info(f"Score for article {article_id} fetched successfully")
    return article.get("score") if article else None

async def delete_article_by_id(article_id: str):
    logger.info(f"Article {article_id} deleted successfully")
    return await collection.delete_one({"_id": article_id})