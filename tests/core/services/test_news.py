import asyncio
from datetime import datetime, timezone

from app.core.services.news import NewsFetcher, normalize_fmp_published_at


def test_normalize_fmp_published_at_uses_configured_source_timezone():
	normalized = normalize_fmp_published_at(
		"2026-10-02 12:31:18", "America/New_York"
	)

	assert normalized == datetime(2026, 10, 2, 16, 31, 18, tzinfo=timezone.utc)


def test_process_fmp_article_persists_sentiment_distribution():
	fetcher = NewsFetcher.__new__(NewsFetcher)
	fetcher.text_metrics = type(
		"Metrics", (), {"analyze_sentiment": lambda self, text: {
			"positive": 0.7,
			"negative": 0.1,
			"neutral": 0.2,
		}}
	)()

	article = asyncio.run(
		fetcher.process_fmp_article(
			{
				"title": "Example article",
				"url": "https://publisher.example/article",
				"publishedDate": "2026-10-02 12:31:18",
				"text": "Example content",
				"symbol": "AAPL",
			}
		)
	)

	assert article.article_id.startswith("fmp_")
	assert article.published_at == datetime(2026, 10, 2, 12, 31, 18, tzinfo=timezone.utc)
	assert article.ingested_at is not None
	assert article.sentiment == "positive"
	assert article.sentiment_probabilities == {
		"positive": 0.7,
		"negative": 0.1,
		"neutral": 0.2,
	}
