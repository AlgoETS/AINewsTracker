# -*- coding: utf-8 -*-
from typing import Optional

from bson.objectid import ObjectId

from app.core.database import MongoDB
from app.models.article import Article


def create_article(article: Article):
    article_dict = article.dict()
    article_dict["_id"] = str(ObjectId())  # Convert ObjectId to a string
    result = MongoDB().get_collection("articles").insert_one(article_dict)
    return result.inserted_id

def create_articles(articles: list[Article]):
    article_dicts = [article.dict() for article in articles]
    for article_dict in article_dicts:
        article_dict["_id"] = str(ObjectId())  # Convert ObjectId to a string
    result = MongoDB().get_collection("articles").insert_many(article_dicts)
    return result.inserted_ids

def get_all_articles() -> list[Article]:
    articles = MongoDB().get_collection("articles").find()
    return [Article(**article) for article in articles]


def get_article_by_id(article_id: str) -> Optional[Article]:
    article = MongoDB().get_collection("articles").find_one({"_id": article_id})
    return Article(**article) if article else None


def get_articles_by_company_id(company_id: str) -> list[Article]:
    articles = MongoDB().get_collection("articles").find({"company_id": company_id})
    return [Article(**article) for article in articles]

def get_score_by_article_id(article_id: str) -> int:
    article = MongoDB().get_collection("articles").find_one({"article_id": article_id})
    if article is not None:
        score = article.get("score")
        if score is not None:
            return int(score)
    return None

def delete_article_by_id(article_id: str):
    result = MongoDB().get_collection("articles").delete_one({"_id": article_id})
    return result.deleted_count

