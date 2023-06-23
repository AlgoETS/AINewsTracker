# -*- coding: utf-8 -*-
import httpx
import csv
from datetime import datetime
from typing import List

from app.config import settings
from app.core.repo.news import create_news
from app.models.news import News

class NewsSeeder:
    API_KEY = settings.API_KEY
    NEWS_URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

    @staticmethod
    def generate_csv(news_list: List[News], filename: str):
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
    async def get_news_data(cls):
        async with httpx.AsyncClient() as client:
            response = await client.get(cls.NEWS_URL)
        return response.json()

    @staticmethod
    def create_news(data: List[dict]) -> List[News]:
        news_list = []
        for news_data in data:
            news_item = News(
                source_name=news_data["source"]["name"],
                topics=[],
                country=news_data.get("country", ""),
                language=news_data.get("language", ""),
                type=news_data.get("type", ""),
                source_url=news_data["url"],
                id=news_data["source"]["id"],
                link=news_data["url"],
                data=news_data,
                number_of_articles=0,
                last_fetch=datetime.now(),
                last_update=datetime.now(),
                last_article=datetime.now()
            )
            news_list.append(news_item)
        return news_list

    @classmethod
    async def get_news_and_save_to_csv(cls, filename: str):
        data = await cls.get_news_data()
        news_list = cls.create_news(data["articles"])
        cls.generate_csv(news_list, filename)

    @classmethod
    async def seed_news(cls):
        data = await cls.get_news_data()
        news_list = cls.create_news(data["articles"])
        create_news(news_list)