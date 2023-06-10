from fastapi import APIRouter
from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from ..models import Article, Score
from .database import collection_articles, collection_scores

router = APIRouter()


@router.post("/articles")
def create_article(article: Article):
    article_dict = article.dict()
    article_dict["_id"] = str(ObjectId())
    result = collection_articles.insert_one(article_dict)
    return result.inserted_id


@router.get("/articles")
def get_all_articles():
    articles = collection_articles.find()
    return [Article(**article) for article in articles]


@router.get("/articles/{article_id}")
def get_article(article_id: str):
    article = collection_articles.find_one({"_id": article_id})
    return Article(**article) if article else None


@router.put("/articles/{article_id}")
def update_article(article_id: str, updated_article: Article):
    updated_article_dict = updated_article.dict()
    collection_articles.update_one({"_id": article_id}, {"$set": updated_article_dict})
    return {"message": "Article updated successfully"}


@router.delete("/articles/{article_id}")
def delete_article(article_id: str):
    collection_articles.delete_one({"_id": article_id})
    return {"message": "Article deleted successfully"}


@router.get("/articles/{article_id}/score")
def get_score_by_article_id(article_id: str):
    score = collection_scores.find_one({"article_id": article_id})
    return Score(**score) if score else None


@router.post("/articles/{article_id}/score")
def create_score(article_id: str, score: Score):
    score_dict = score.dict()
    score_dict["_id"] = str(ObjectId())
    score_dict["article_id"] = article_id
    result = collection_scores.insert_one(score_dict)
    return result.inserted_id
