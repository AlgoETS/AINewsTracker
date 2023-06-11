# -*- coding: utf-8 -*-
from typing import Optional

from bson.objectid import ObjectId

from app.core.database import collection_articles
from app.models.article import Article, Score


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


def create_score(score: Score):
    score_dict = score.dict()
    score_dict["_id"] = str(ObjectId())  # Convert ObjectId to a string
    result = collection_articles.insert_one(score_dict)
    return result.inserted_id


def get_score_by_article_id(article_id: str) -> Optional[Score]:
    score = collection_articles.find_one({"article_id": article_id})
    return Score(**score) if score else None
