# -*- coding: utf-8 -*-
import httpx
import csv
from datetime import datetime
from typing import List
from app.config import Settings
from app.core.repo.article import create_article
from app.models.article import Article
from app.core.services.news import NewsFetcher
import os
class NewsSeeder:
    settings = Settings()
    API_KEY = settings.FMP_API_KEY
    NEWS_URL = f"https://financialmodelingprep.com/api/v3/stock_news?page=0&apikey={API_KEY}"

    @staticmethod
    def generate_csv(news_list: List[Article], filename: str):
        with open(filename, "w", newline="") as csvfile:
            fieldnames = [
                "source_name",
                "topics",
                "country",
                "language",
                "type",
                "source_url",
                "id",
                "link",
                "data",
                "number_of_articles",
                "last_fetch",
                "last_update",
                "last_article",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for news_item in news_list:
                writer.writerow(news_item.dict())
    
    @classmethod
    async def get_news_data(cls, tickers: str = "", page: int = 0):
        tickers_param = f"tickers={tickers}&" if tickers else ""
        url = f"https://financialmodelingprep.com/api/v3/stock_news?{tickers_param}page={page}&apikey={cls.API_KEY}"

        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url)
                response.raise_for_status()  # Raise an exception if an HTTP error occurred
                return {"articles": response.json()[:2]}
                
            except httpx.RequestError as e:
                print(f"Error making the request: {e}")
            except httpx.HTTPStatusError as e:
                print(f"HTTP error occurred: {e}")
            except Exception as e:
                print(f"An error occurred: {e}")
            return []
    


    @classmethod
    async def create_news(cls,data: List[dict]) -> List[Article]:
        articles = []
        for article in data:
            article_processed = await NewsFetcher().process_fmp_article(article)
            articles.append(article_processed)
        return articles

    @classmethod
    async def get_news_and_save_to_csv(cls, filename: str):
        data = await cls.get_news_data()
        news_list = cls.create_news(data["articles"])
        cls.generate_csv(news_list, filename)

    @classmethod
    async def seed_news(cls):
        data = await cls.get_news_data()
        news_list = await  cls.create_news(data["articles"])
        await create_article(news_list)