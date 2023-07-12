# -*- coding: utf-8 -*-
from typing import List
from fastapi import APIRouter, HTTPException, BackgroundTasks

from app.seed.news import NewsSeeder
from app.seed.companies import CompanySeeder

from app.core.logging import Logger
import logging
from typing import List

logger = Logger(logging.INFO).get_logger()

router = APIRouter(
    prefix="/seed",
    tags=["Seed"],
    responses={404: {"description": "Not found"}},
)

@router.post("/seed_news")
async def seed_news(background_tasks: BackgroundTasks):
    background_tasks.add_task(NewsSeeder.seed_news)
    return {"message": "Seeding news in background"}

@router.post("/seed_companies")
async def seed_companies(background_tasks: BackgroundTasks):
    background_tasks.add_task(CompanySeeder.seed_companies)
    return {"message": "Seeding companies in background"}