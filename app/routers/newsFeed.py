# -*- coding: utf-8 -*-
# news_feed_routes.py
from app.core.repo.newsFeed import create_newsFeed, get_newsFeed_by_id, update_newsFeed_by_id, delete_newsFeed_by_id
from fastapi import APIRouter

from app.models import NewsFeed

router = APIRouter(
    prefix="/newsFeed",
    tags=["NewsFeed"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=NewsFeed)
async def create_feed(newsFeed: NewsFeed):
    feed_id = create_newsFeed(newsFeed)
    return {**newsFeed.dict(), "_id": feed_id}


@router.get("/{newsFeed_id}", response_model=NewsFeed)
async def read_feed(newsFeed_id: str):
    return get_newsFeed_by_id(newsFeed_id)


@router.put("/{newsFeed_id}", response_model=NewsFeed)
async def update_feed(newsFeed_id: str, newsFeed: NewsFeed):
    update_newsFeed_by_id(newsFeed_id, newsFeed)
    return {**newsFeed.dict(), "_id": newsFeed_id}


@router.delete("/{newsFeed_id}")
async def delete_feed(newsFeed_id: str):
    delete_newsFeed_by_id(newsFeed_id)
    return {"message": f"News Feed {newsFeed_id} has been deleted."}
