# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import List

from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["financial_data"]
collection_names = ["companies", "articles", "scores", "rss_feeds"]
collections = {name: db[name] for name in collection_names}


# Models
class Company(BaseModel):
    name: str
    ticker: str


class Article(BaseModel):
    title: str
    content: str
    url: str
    date: datetime
    company_id: str


class Score(BaseModel):
    sentiment_score: float
    sentiment: str
    article_id: str


class RSSFeed(BaseModel):
    link: str
    data: str
    last_fetch: datetime


app = FastAPI()


# Routes
@app.post("/companies")
def create_company(company: Company):
    company_dict = company.dict()
    company_dict["_id"] = company_dict["ticker"]
    collections["companies"].insert_one(company_dict)
    return {"message": "Company created successfully"}


@app.post("/articles")
def create_article(article: Article):
    article_dict = article.dict()
    collections["articles"].insert_one(article_dict)
    return {"message": "Article created successfully"}


@app.post("/scores")
def create_score(score: Score):
    score_dict = score.dict()
    collections["scores"].insert_one(score_dict)
    return {"message": "Score created successfully"}


@app.post("/rss_feeds")
def create_rss_feed(rss_feed: RSSFeed):
    rss_feed_dict = rss_feed.dict()
    collections["rss_feeds"].insert_one(rss_feed_dict)
    return {"message": "RSS Feed created successfully"}


@app.get("/companies/{ticker}/articles")
def get_articles_by_company(ticker: str):
    articles = list(collections["articles"].find({"company_id": ticker}))
    return {"articles": articles}


@app.get("/articles/{article_id}/scores")
def get_scores_by_article(article_id: str):
    scores = list(collections["scores"].find({"article_id": article_id}))
    return {"scores": scores}


@app.get("/rss_feeds/{feed_id}")
def get_rss_feed(feed_id: str):
    rss_feed = collections["rss_feeds"].find_one({"_id": feed_id})
    return {"rss_feed": rss_feed}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
