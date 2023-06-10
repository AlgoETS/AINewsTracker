from typing import Callable, List
import httpx
from app.core.database import MongoDB


def execute_trading_strategy(
    companies_to_follow: List[str],
    fetch_news: Callable[[str], List[dict]],
    analyze_sentiment: Callable[[dict], float],
    buy_stock: Callable[[str], None],
    sell_stock: Callable[[str], None],
    sentiment_threshold: float,
    buy_sell_percentage: float
):
    for company in companies_to_follow:
        news_articles = fetch_news(company)

        positive_count = 0
        negative_count = 0

        for article in news_articles:
            sentiment_score = analyze_sentiment(article)

            if sentiment_score > sentiment_threshold:
                positive_count += 1
            elif sentiment_score < -sentiment_threshold:
                negative_count += 1

        total_count = len(news_articles)

        if total_count > 0:
            positive_ratio = positive_count / total_count
            negative_ratio = negative_count / total_count

            if positive_ratio > buy_sell_percentage:
                buy_stock(company)
            elif negative_ratio > buy_sell_percentage:
                sell_stock(company)
