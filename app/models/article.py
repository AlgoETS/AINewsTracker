from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .database import collection_articles
from bson import ObjectId
from .models import Article

class Article(BaseModel):
    title: str
    content: str
    url: str
    date: datetime
    score_id: Optional[str] = None
    company_id: Optional[str] = None


def create_article(article: Article):
    article_dict = article.dict()
    article_dict["_id"] = str(ObjectId())  # Convert ObjectId to a string
    result = collection_articles.insert_one(article_dict)
    return result.inserted_id

def get_article_by_id(article_id: str) -> Optional[Article]:
    article = collection_articles.find_one({"_id": article_id})
    return Article(**article) if article else None

def get_articles_by_company_id(company_id: str) -> list[Article]:
    articles = collection_articles.find({"company_id": company_id})
    return [Article(**article) for article in articles]
