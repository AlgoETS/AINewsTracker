# -*- coding: utf-8 -*-
from fastapi import APIRouter

router = APIRouter()


@router.get("/execute_trading_strategy/{company}")
def execute_trading_strategy(company: str):
    fetch_news = fetch_news_function
    analyze_sentiment = analyze_sentiment_function
    buy_stock = buy_stock_function
    sell_stock = sell_stock_function
    sentiment_threshold = 0.5
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

        buy_sell_percentage = 0.7

        if positive_ratio > buy_sell_percentage:
            buy_stock(company)
        elif negative_ratio > buy_sell_percentage:
            sell_stock(company)

    return {"message": "Trading strategy executed"}
