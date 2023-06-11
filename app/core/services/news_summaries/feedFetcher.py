from datetime import datetime
import uuid
import requests
from bs4 import BeautifulSoup
import feedparser
import time

from ..sentiments import analyze_sentiment 
from ..summarizer import summarize_text
from ...repo.article import Article
from ..topic_classification import classify_topic

class FeedFetcher:
    def __init__(self):
        pass

    def fetch_feed_entries(self, source, limit):
        response = requests.get(source.url)
        feed = response.text
        parsed_feed = feedparser.parse(feed)
        entries = parsed_feed.entries[:limit]
        articles = []
        for entry in entries:
            text_content=self.get_entry_text(entry['link'])
            sentiment=analyze_sentiment(text_content)
            most_sentiment = max(sentiment, key=sentiment.get)
            most_sentiment_score = sentiment[most_sentiment]
            article = Article(
                id=str(uuid.uuid4()),
                title=entry.get('title'),
                content=text_content,
                url=entry.get('link'),
                date= datetime.fromtimestamp(time.mktime(entry.get('published_parsed'))),
                sentiment = most_sentiment,
                sentiment_score= most_sentiment_score,
                summary=summarize_text(text_content),
                topic=classify_topic(text_content),
            )
            articles.append(article)
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
