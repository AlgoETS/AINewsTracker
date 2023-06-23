from typing import Optional, List
from app.core.database.db import MongoDB
from app.models.article import Article
from bson.objectid import ObjectId

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


async def get_all_articles() -> list[Article]:
    articles = await collection.find().to_list(length=100)
    return [Article(**article) for article in articles]

async def get_article_by_id(article_id: str) -> Optional[Article]:
    article = await collection.find_one({"_id": article_id})
    return Article(**article) if article else None

async def get_articles_by_company_id(company_id: str) -> list[Article]:
    articles = await collection.find({"company_id": company_id}).to_list(length=100)
    return [Article(**article) for article in articles]

async def get_score_by_article_id(article_id: str) -> int:
    article = await collection.find_one({"article_id": article_id}, {"score": 1})
    return article.get("score") if article else None

async def delete_article_by_id(article_id: str):
    return await collection.delete_one({"_id": article_id})
