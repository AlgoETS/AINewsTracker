from datetime import datetime
import requests
from bs4 import BeautifulSoup
import feedparser
import time

from ...models.article import Article


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
            article = Article(
                title=entry.get('title'),
                content=self.get_entry_text(entry['link']),
                url=entry.get('link'),
                date= datetime.fromtimestamp(time.mktime(entry.get('published_parsed'))),
                
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
