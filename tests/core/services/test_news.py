import pytest
from unittest.mock import Mock, AsyncMock
from app.core.services.news import NewsFetcher
from app.models.article import Article


@pytest.fixture
def mock_news_fetcher():
    # Create a NewsFetcher instance with mocked methods
    news_fetcher = NewsFetcher()
    news_fetcher.client.get = AsyncMock()
    news_fetcher.text_metrics.analyze_sentiment = Mock()
    news_fetcher.text_metrics.detect_ticker = Mock()
    news_fetcher.text_metrics.classify_topic = Mock()
    news_fetcher.text_metrics.summarize_text = Mock()
    return news_fetcher

@pytest.mark.asyncio
async def test_process_article(mock_news_fetcher):
    # Mock response data
    article_data = {"id": "1", "title": "test", "url": "http://test.com", "publishedAt": "2023-06-28T00:00:00"}
    content = "Test article content."

    # Set return values for mocked methods
    mock_news_fetcher.text_metrics.analyze_sentiment.return_value = {"positive": 0.5, "negative": 0.2, "neutral": 0.3}
    mock_news_fetcher.text_metrics.detect_ticker.return_value = ["TST"]
    mock_news_fetcher.text_metrics.classify_topic.return_value = ["Test"]
    mock_news_fetcher.text_metrics.summarize_text.return_value = "Summary of the test article."

    # Call the method under test
    result = await mock_news_fetcher.process_article(article_data, content)

    # Assert that the result is as expected
    expected_result = Article(
        id="1",
        title="test",
        content=content,
        url="http://test.com",
        date="2023-06-28T00:00:00",
        sentiment="positive",
        sentiment_score=0.5,
        summary="Summary of the test article.",
        topic=["Test"],
        ticker=["TST"],
    )
    assert result == expected_result
