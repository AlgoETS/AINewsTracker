# -*- coding: utf-8 -*-
from fastapi import APIRouter, HTTPException

from app.core.repo.article import (
    create_article,
    delete_article_by_id,
    get_all_articles,
    get_article_by_id,
    get_score_by_article_id,
)
from app.models import Article

router = APIRouter(
    prefix="/articles",
    tags=["Articles"],
    responses={404: {"description": "Not found"}},
)


@router.post("/articles")
def create_article_handler(article: Article):
    article_id = create_article(article)
    return {"message": "Article created successfully", "article_id": article_id}


@router.get("/articles", response_model=list[Article])
def get_all_articles_handler():
    return get_all_articles()


@router.get("/articles/{article_id}")
def get_article_handler(article_id: str):
    if article := get_article_by_id(article_id):
        return article
    else:
        raise HTTPException(status_code=404, detail="Article not found")


@router.delete("/articles/{article_id}")
def delete_article_handler(article_id: str):
    deleted_count = delete_article_by_id(article_id)
    if deleted_count == 0:
        raise HTTPException(status_code=404, detail="Article not found")
    else:
        return {"message": "Article deleted successfully", "article_id": article_id}


@router.get("/articles/{article_id}/score")
def get_score_by_article_id_handler(article_id: str):
    score = get_score_by_article_id(article_id)
    if score is None:
        raise HTTPException(status_code=404, detail="Score not found")
    else:
        return {"score": score}
