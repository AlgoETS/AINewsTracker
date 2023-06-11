from datetime import datetime
import requests
from bs4 import BeautifulSoup
import feedparser
import time

from app.core.services.finbert import analyze_sentiment

from app.models.article import Article
from app.core.repo.article import create_articles


class RSSFeed:
    def __init__(self):
        pass

    def fetch_feed_entries(self, source, limit):
        response = requests.get(source.url)
        feed = response.text
        parsed_feed = feedparser.parse(feed)
        entries = parsed_feed.entries[:limit]
        articles = []
        for entry in entries:
            print(entry)
            text_content=self.get_entry_text(entry['link'])
            try:
                sentiment=analyze_sentiment(text_content)
            except Exception:
                sentiment = {'Neutral': 0.5}
            most_sentiment = max(sentiment, key=sentiment.get)
            most_sentiment_score = sentiment[most_sentiment]
            article = Article(
                id=entry.get('id'),
                title=entry.get('title'),
                content=text_content,
                url=entry.get('link'),
                date= datetime.fromtimestamp(time.mktime(entry.get('published_parsed'))),
                sentiment = most_sentiment,
                sentiment_score= most_sentiment_score,
            )
            articles.append(article)
        create_articles(articles)
        return articles

    def get_entry_text(self, link):
        response = requests.get(link)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        # Find and remove unwanted elements
        unwanted_tags = ['nav', 'footer', 'header', 'aside', 'script', 'style', 'form', 'input', 'button', 'img', 'iframe', 'video', 'audio', 'svg', 'select', 'label', 'textarea', 'object', 'embed', 'noscript', 'meta']

        for tag in unwanted_tags:
            for elem in soup.find_all(tag):
                elem.decompose()

        # Get the text content
        text = soup.get_text(separator=' ')
        return text.strip() if text else None