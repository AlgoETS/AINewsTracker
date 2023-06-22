# -*- coding: utf-8 -*-
import time
from datetime import datetime

import feedparser
import httpx
from bs4 import BeautifulSoup

from app.core.repo.article import create_articles
from app.core.services.sentiments import analyze_sentiment
from app.core.services.topic_classification import classify_topic
from app.models.article import Article


class FeedFetcher:
    def __init__(self):
        self.client = httpx.AsyncClient()  # initialize the AsyncClient
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

    async def fetch_feed_entries(self, source, limit):
        response = await self.client.get(source.url)
        feed = response.text
        parsed_feed = feedparser.parse(feed)
        entries = parsed_feed.entries[:limit]
        articles = []
        for entry in entries:
            print(entry)
            text_content = await self.get_entry_text(entry["link"])
            try:
                sentiment = analyze_sentiment(text_content)
            except Exception:
                sentiment = {"Neutral": 0.5}
            most_sentiment = max(sentiment, key=sentiment.get)
            most_sentiment_score = sentiment[most_sentiment]
            article = Article(
                id=entry.get("id"),
                title=entry.get("title"),
                content=text_content,
                url=entry.get("link"),
                date=datetime.fromtimestamp(time.mktime(entry.get("published_parsed"))),
                sentiment=most_sentiment,
                sentiment_score=most_sentiment_score,
                summary=summarize_text(text_content),
                topic=classify_topic(text_content),
            )
            articles.append(article)
        await create_articles(articles)
        return articles

    async def get_entry_text(self, link):
        response = await self.client.get(link)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")

        for tag in self.unwanted_tags:
            for elem in soup.find_all(tag):
                elem.decompose()

        # Get the text content
        text = soup.get_text(separator=" ")
        return text.strip() if text else None
