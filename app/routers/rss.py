# -*- coding: utf-8 -*-
from fastapi import APIRouter

from app.core.services.rss.rss import RSSFeed
from app.core.services.rss.source import (
    CNBC,
    FT,
    WSJ,
    CNNMoney,
    Fortune,
    Investing,
    MarketWatch,
    Nasdaq,
    Reddit,
    Reuters,
    SeekingAlpha,
    Yahoo,
    Zacks,
)

router = APIRouter(
    prefix="/rss",
    tags=["RSS"],
    responses={404: {"description": "Not found"}},
)
rss_feed = RSSFeed()

sources = {
    "CNBC": CNBC(),
    "Seeking Alpha": SeekingAlpha(),
    "Investing.com": Investing(),
    "Nasdaq": Nasdaq(),
    "WSJ": WSJ(),
    "Yahoo Finance": Yahoo(),
    "FT": FT(),
    "Fortune": Fortune(),
    "MarketWatch": MarketWatch(),
    "Zacks": Zacks(),
    "Reddit": Reddit(),
    "CNNMoney": CNNMoney(),
    "Reuters": Reuters(),
}


@router.post("/rss/feed")
async def fetch_rss_feed(source: str, limit: int):
    # get source from name
    source = sources[source]
    return await rss_feed.fetch_feed_entries(source, limit)
