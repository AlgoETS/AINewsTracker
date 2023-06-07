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
    data = response.json()
    
    return data
