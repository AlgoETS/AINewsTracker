from typing import Optional
from app.core.database.db import MongoDB
from app.models.article import Article
from bson.objectid import ObjectId

# Initialize MongoDB connection
mongo_db = MongoDB()
collection = mongo_db.get_collection("articles")

async def create_article(article: Article):
    article_dict = article.dict()
    article_dict["_id"] = str(ObjectId())
    return await collection.insert_one(article_dict)

async def create_articles(articles: list[Article]):
    articles = [dict(item.dict(), _id=str(ObjectId())) for item in articles]
    return await collection.insert_many(articles)

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
