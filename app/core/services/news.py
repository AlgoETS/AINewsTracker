# -*- coding: utf-8 -*-
import httpx
import logging
import time
from datetime import datetime, timezone
from hashlib import sha256
from urllib.parse import urlparse
from zoneinfo import ZoneInfo
import feedparser
from bs4 import BeautifulSoup
from app.config import Settings
from app.core.logging import Logger

from app.core.repo.article import create_article
from app.core.services.metrics import TextMetrics
from app.models.article import Article

logger = Logger(logging.INFO).get_logger()
settings = Settings()


def normalize_fmp_published_at(value: str, source_timezone: str) -> datetime:
    published_at = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if published_at.tzinfo is None:
        published_at = published_at.replace(tzinfo=ZoneInfo(source_timezone))
    return published_at.astimezone(timezone.utc)


class NewsFetcher:
    def __init__(self):
        self.client = httpx.AsyncClient()
        self.text_metrics = TextMetrics()
        self.unwanted_tags = [
            "nav",
            "footer",
            "header",
            "aside",
            "script",
            "style",
            "form",
            "input",
            "button",
            "img",
            "iframe",
            "video",
            "audio",
            "svg",
            "select",
            "label",
            "textarea",
            "object",
            "embed",
            "noscript",
            "meta",
        ]

    async def process_article(self, article_data: dict, content: str):
        sentiment = self.text_metrics.analyze_sentiment(content)
        most_sentiment = max(sentiment, key=sentiment.get)
        most_sentiment_score = sentiment[most_sentiment]
        detected_tickers = self.text_metrics.detect_ticker(content)
        topics = self.text_metrics.classify_topic(content)
        summary = self.text_metrics.summarize_text(content)
        return Article(
            title=article_data["title"],
            url=article_data["link"],
            publishedDate=article_data["published"],
            text=content,
            source_name=article_data["source_name"],
            sentiment_score=most_sentiment_score,
            sentiment=most_sentiment,
            author=article_data.get("author"),
            likes=article_data.get("likes"),
            comments=article_data.get("comments"),
            tickers=detected_tickers,
            topics=topics,
            summary=summary,
        )

    async def fetch_rss_feed(self, api_key, start_date, end_date, limit=10):
        url = "https://financialmodelingprep.com/api/v4/rss_feed_8k"

        params = {
            "from": start_date.strftime("%Y-%m-%d"),
            "to": end_date.strftime("%Y-%m-%d"),
            "limit": limit,
            "apikey": api_key,
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
        rss_feed_data = response.json()

        articles = []
        for article_data in rss_feed_data:
            content = await self.get_entry_text(article_data["link"])
            if content is not None:
                article = await self.process_article(article_data, content)
                articles.append(article)

        await create_article(articles)
        return articles

    async def fetch_gnews_articles(self, api_key: str, query: str, lang: str, country: str, max_results: int):
        url = f"https://gnews.io/api/v4/search?q={query}&lang={lang}&country={country}&max={max_results}&apikey={api_key}"
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
        data = response.json()
        articles_data = data["articles"]
        articles = []

        for article_data in articles_data:
            logger.info(f"Processing article: {article_data}")
            text_content = await self.get_entry_text(article_data["url"])
            article = await self.process_article(article_data, text_content)
            articles.append(article)

        await create_article(articles)
        return articles

    async def fetch_feed_entries(self, source, limit):
        try:
            response = await self.client.get(source.url)
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            logger.error(f"Failed to fetch feed from {source.url} due to {e}")
            return []

        feed = response.text
        parsed_feed = feedparser.parse(feed)
        entries = parsed_feed.entries[:limit]
        articles = []

        for entry in entries:
            logger.info(f"Processing entry: {entry}")
            text_content = await self.get_entry_text(entry["link"])
            article = await self.process_article(entry, text_content)
            articles.append(article)

        await create_article(articles)
        return articles

    async def get_entry_text(self, link):
        try:
            response = await self.client.get(link)
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            logger.error(f"Failed to fetch entry from {link} due to {e}")
            return ""

        html = response.text
        soup = BeautifulSoup(html, "html.parser")

        for tag in self.unwanted_tags:
            for elem in soup.find_all(tag):
                elem.decompose()

        # Get the text content
        text = soup.get_text(separator=" ")
        return text.strip() if text else None

    def extract_source(self,url: str) -> str:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        if domain.startswith("www."):
            domain = domain[4:]
        return domain

    async def process_fmp_article(self, article_dict: dict):
        content = article_dict.get("text")
        sentiment = self.text_metrics.analyze_sentiment(content)
        most_sentiment = max(sentiment, key=sentiment.get)
        most_sentiment_score = sentiment[most_sentiment]
        published_date = article_dict["publishedDate"]
        article_dict["source_name"] = self.extract_source(article_dict["url"])
        article_dict["article_id"] = f"fmp_{sha256(article_dict['url'].encode()).hexdigest()}"
        article_dict["published_at"] = normalize_fmp_published_at(
            published_date, settings.FMP_PUBLISHED_DATE_TIMEZONE
        )
        article_dict["ingested_at"] = datetime.now(timezone.utc)
        article_dict["sentiment"] = most_sentiment
        article_dict["sentiment_score"] = most_sentiment_score
        article_dict["sentiment_probabilities"] = sentiment
        model_config = getattr(getattr(self.text_metrics, "sentiment_model", None), "config", None)
        article_dict["model_name"] = getattr(
            model_config, "_name_or_path", "ProsusAI/finbert"
        )
        article_dict["model_version"] = getattr(
            model_config, "_commit_hash", None
        ) or "unknown"
        article_dict["tickers"] = [article_dict["symbol"]]
        return Article(**article_dict)
