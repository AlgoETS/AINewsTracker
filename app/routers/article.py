# -*- coding: utf-8 -*-
import logging
from fastapi import APIRouter, HTTPException, Request
from app.core.logging import Logger

logger = Logger(logging.INFO).get_logger()

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

@router.post("/")
def create_article_handler(article: Article):
    article_id = create_article(article)
    logger.info(f"Article {article_id} created successfully")
    return {"message": "Article created successfully", "article_id": article_id}

@router.get("/", response_model=list[Article])
def get_all_articles_handler():
    logger.info("Fetching all articles")
    return get_all_articles()

@router.get("/{article_id}")
def get_article_handler(article_id: str):
    if article := get_article_by_id(article_id):
        logger.info(f"Article {article_id} fetched successfully")
        return article
    else:
        logger.error(f"Article {article_id} not found")
        raise HTTPException(status_code=404, detail="Article not found")

@router.delete("/{article_id}")
def delete_article_handler(article_id: str):
    deleted_count = delete_article_by_id(article_id)
    if deleted_count == 0:
        logger.error(f"Article {article_id} not found")
        raise HTTPException(status_code=404, detail="Article not found")
    else:
        logger.info(f"Article {article_id} deleted successfully")
        return {"message": "Article deleted successfully", "article_id": article_id}

@router.get("/{article_id}/score")
def get_score_by_article_id_handler(article_id: str):
    score = get_score_by_article_id(article_id)
    if score is None:
        logger.error(f"Score for article {article_id} not found")
        raise HTTPException(status_code=404, detail="Score not found")
    else:
        logger.info(f"Score for article {article_id} fetched successfully")
        return {"score": score}
