from pydantic import BaseModel
from typing import Optional
from .database import collection_scores
from bson import ObjectId
from .models import Score

class Score(BaseModel):
    sentiment_score: float
    sentiment: str
    article_id: str
      
def create_score(score: Score):
    score_dict = score.dict()
    score_dict["_id"] = str(ObjectId())  # Convert ObjectId to a string
    result = collection_scores.insert_one(score_dict)
    return result.inserted_id

def get_score_by_article_id(article_id: str) -> Optional[Score]:
    score = collection_scores.find_one({"article_id": article_id})
    return Score(**score) if score else None
