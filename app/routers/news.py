# -*- coding: utf-8 -*-
from typing import List
from fastapi import APIRouter, HTTPException, BackgroundTasks

from app.core.repo.news import (
    create_news,
    delete_news_by_id,
    get_news_by_id,
    get_news_by_name,
    update_news_by_id,
)
from app.core.services.news import NewsFetcher
from app.models import News

from app.core.logging import Logger
import logging

logger = Logger(logging.INFO).get_logger()

router = APIRouter(
    prefix="/news",
    tags=["News"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=News)
async def create_news_item(news: News):
    news_id = create_news(news)
    logger.info(f"News item {news_id} created successfully")
    return {**news.dict(), "_id": news_id}

@router.get("/{news_id}", response_model=News)
async def read_news(news_id: str):
    news_item = get_news_by_id(news_id)
    if news_item is None:
        logger.error(f"News item {news_id} not found")
        raise HTTPException(status_code=404, detail="News not found")
    logger.info(f"News item {news_id} fetched successfully")
    return news_item

@router.get("/{news_name}", response_model=list[News])
async def read_news_by_name(news_name: str):
    news_items = get_news_by_name(news_name)
    if not news_items:
        logger.error(f"No news items found with name {news_name}")
        raise HTTPException(status_code=404, detail="News not found")
    logger.info(f"News items with name {news_name} fetched successfully")
    return news_items

@router.put("/{news_id}", response_model=News)
async def update_news_item(news_id: str, news: News):
    if not update_news_by_id(news_id, news):
        logger.error(f"News item {news_id} could not be updated")
        raise HTTPException(status_code=404, detail="News not found")
    logger.info(f"News item {news_id} updated successfully")
    return {**news.dict(), "_id": news_id}

@router.delete("/{news_id}")
async def delete_news_item(news_id: str):
    if not delete_news_by_id(news_id):
        logger.error(f"News item {news_id} could not be deleted")
        raise HTTPException(status_code=404, detail="News not found")
    logger.info(f"News item {news_id} deleted successfully")
    return {"message": f"News item {news_id} has been deleted."}

# Additional endpoints for the NewsFetcher
news_fetcher = NewsFetcher()

@router.get("/rss/{api_key}/{start_date}/{end_date}", response_model=List[News])
async def fetch_rss(api_key: str, start_date: str, end_date: str):
    return await news_fetcher.fetch_rss_feed(api_key, start_date, end_date)

@router.get("/gnews/{api_key}/{query}/{lang}/{country}/{max_results}", response_model=List[News])
async def fetch_gnews(api_key: str, query: str, lang: str, country: str, max_results: int):
    return await news_fetcher.fetch_gnews_articles(api_key, query, lang, country, max_results)

@router.get("/entries/{source}/{limit}", response_model=List[News])
async def fetch_entries(background_tasks: BackgroundTasks, source: str, limit: int):
    if limit > 10:
        background_tasks.add_task(news_fetcher.fetch_feed_entries, source, limit)
        return {"message": "The task is running in the background."}
    return await news_fetcher.fetch_feed_entries(source, limit)
