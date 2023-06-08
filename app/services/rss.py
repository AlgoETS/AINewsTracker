import httpx
from datetime import datetime

async def fetch_rss_feed(api_key, start_date, end_date, limit=10):
    url = "https://financialmodelingprep.com/api/v4/rss_feed_8k"

    params = {
        "from": start_date.strftime('%Y-%m-%d'),
        "to": end_date.strftime('%Y-%m-%d'),
        "limit": limit,
        "apikey": api_key
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
    return response.json()

async def fetch_articles(api_key: str, query: str, lang: str, country: str, max_results: int):
    url = f'https://gnews.io/api/v4/search?q={query}&lang={lang}&country={country}&max={max_results}&apikey={api_key}'
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    data = response.json()
    return data['articles']

async def print_articles(api_key: str, query: str, lang: str, country: str, max_results: int):
    articles = await fetch_articles(api_key, query, lang, country, max_results)
    for article in articles:
        print("Title: ", article['title'])
        print("Description: ", article['description'])
