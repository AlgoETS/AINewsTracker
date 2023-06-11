from fastapi import APIRouter
from pydantic import BaseModel
from bson import ObjectId
from ..core.services.rss.source import Source, CNBC, SeekingAlpha, Investing, Nasdaq, WSJ, Yahoo, FT, Fortune,MarketWatch,Zacks,Reddit,CNNMoney,Reuters
from ..core.services.rss.rss import RSSFeed

router = APIRouter(
    prefix="/rss",
    tags=["rss"],
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
def fetch_rss_feed(source: str , limit: int):
    # get source from name
    source = sources[source]
    return rss_feed.fetch_feed_entries(source, limit)