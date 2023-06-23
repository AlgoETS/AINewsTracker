# -*- coding: utf-8 -*-
from typing import Callable, List
import logging

from backtesting import Backtest, Strategy
from backtesting.lib import crossover

logger = logging.getLogger(__name__)

class SentimentTradingStrategy(Strategy):

    def __init__(self,
                companies_to_follow: List[str],
                fetch_news: Callable[[str], List[dict]],
                analyze_sentiment: Callable[[dict], float],
                buy_stock: Callable[[str], None],
                sell_stock: Callable[[str], None],
                sentiment_threshold: float,
                buy_sell_percentage: float):
        self.companies_to_follow = companies_to_follow
        self.fetch_news = fetch_news
        self.analyze_sentiment = analyze_sentiment
        self.buy_stock = buy_stock
        self.sell_stock = sell_stock
        self.sentiment_threshold = sentiment_threshold
        self.buy_sell_percentage = buy_sell_percentage

    def init(self):
        self.trades = 0

    def next(self):
        self.trades += 1
        if self.trades % 5 == 0:
            self.execute_trading_strategy()

    def execute_trading_strategy(self):
        for company in self.companies_to_follow:
            news_articles = self.fetch_news(company)

            positive_count = 0
            negative_count = 0

            for article in news_articles:
                sentiment_score = self.analyze_sentiment(article)

                if sentiment_score > self.sentiment_threshold:
                    positive_count += 1
                elif sentiment_score < -self.sentiment_threshold:
                    negative_count += 1

            total_count = len(news_articles)

            if total_count > 0:
                positive_ratio = positive_count / total_count
                negative_ratio = negative_count / total_count

                if positive_ratio > self.buy_sell_percentage:
                    logger.info(f"Buying stock for {company}")
                    self.buy_stock(company)
                elif negative_ratio > self.buy_sell_percentage:
                    logger.info(f"Selling stock for {company}")
                    self.sell_stock(company)
