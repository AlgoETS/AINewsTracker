from fastapi import APIRouter
from typing import Optional
from bson import ObjectId
from .models import Score
from .database import collection_scores

router = APIRouter()


@router.get("/scores/{score_id}")
def get_score(score_id: str):
    score = collection_scores.find_one({"_id": score_id})
    return Score(**score) if score else None


@router.put("/scores/{score_id}")
def update_score(score_id: str, updated_score: Score):
    updated_score_dict = updated_score.dict()
    collection_scores.update_one({"_id": score_id}, {"$set": updated_score_dict})
    return {"message": "Score updated successfully"}


@router.delete("/scores/{score_id}")
def delete_score(score_id: str):
    collection_scores.delete_one({"_id": score_id})
    return {"message": "Score deleted successfully"}


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
