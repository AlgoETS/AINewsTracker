# -*- coding: utf-8 -*-
import logging
from fastapi import APIRouter, HTTPException, Request
from app.core.logging import Logger
from typing import List

logger = Logger(logging.INFO).get_logger()

from app.core.repo.article import (
    create_article,
    delete_article_by_id,
    get_all_articles,
    get_article_by_id,
    get_articles_by_company_id,
    get_articles_by_company_ids,
    get_score_by_article_id,
)
from app.models import Article

router = APIRouter(
    prefix="/articles",
    tags=["Articles"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def create_article_handler(article: Article):
    article_id = await create_article(article)
    logger.info(f"Article {article_id} created successfully")
    return {"message": "Article created successfully", "article_id": article_id}

@router.get("/", response_model=List[Article])
async def get_all_articles_handler():
    logger.info("Fetching all articles")
    return await get_all_articles()

@router.get("/{article_id}")
async def get_article_handler(article_id: str):
    if article := await get_article_by_id(article_id):
        logger.info(f"Article {article_id} fetched successfully")
        return article
    else:
        logger.error(f"Article {article_id} not found")
        raise HTTPException(status_code=404, detail="Article not found")

@router.delete("/{article_id}")
async def delete_article_handler(article_id: str):
    deleted_count = await delete_article_by_id(article_id)
    if deleted_count == 0:
        logger.error(f"Article {article_id} not found")
        raise HTTPException(status_code=404, detail="Article not found")
    else:
        logger.info(f"Article {article_id} deleted successfully")
        return {"message": "Article deleted successfully", "article_id": article_id}

@router.get("/{article_id}/score")
async def get_score_by_article_id_handler(article_id: str):
    score = await get_score_by_article_id(article_id)
    if score is None:
        logger.error(f"Score for article {article_id} not found")
        raise HTTPException(status_code=404, detail="Score not found")
    else:
        logger.info(f"Score for article {article_id} fetched successfully")
        return {"score": score}

@router.get("/articles_by_company_id/{company_id}")
async def get_articles_by_company_id_handler(company_id: str):
    articles = await get_articles_by_company_id(company_id)
    if articles is None:
        logger.error(f"Articles for company {company_id} not found")
        raise HTTPException(status_code=404, detail="Articles not found")
    else:
        logger.info(f"Articles for company {company_id} fetched successfully")
        return {
            "articles": articles,
            "company_id": company_id,
        }

@router.post("/articles_by_company_ids")
async def get_articles_by_company_ids_handler(company_ids: List[str]):
    articles = await get_articles_by_company_ids(company_ids)
    if articles is None:
        logger.error(f"Articles for companies {company_ids} not found")
        raise HTTPException(status_code=404, detail="Articles not found")
    else:
        logger.info(f"Articles for companies {company_ids} fetched successfully")
        return {
            "articles": articles,
            "company_ids": company_ids,
        }

