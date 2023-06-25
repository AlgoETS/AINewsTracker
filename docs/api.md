Go to the Swagger Page in /docs

## Execute Trading Strategy

- **Single company** `GET /execute_trading_strategy/{company}`: This endpoint triggers the execution of a trading strategy for a specific company.
- **Multiple companies** `POST /execute_trading_strategy`: This endpoint triggers the execution of a trading strategy for multiple companies.

## News

- **Create news item** `POST /news`: This endpoint creates a new news item.
- **Read news** `GET /news/{news_id}`: This endpoint retrieves a specific news item using its ID.
- **Read news by name** `GET /news/{news_name}`: This endpoint retrieves all news items with a specific name.
- **Update news item** `PUT /news/{news_id}`: This endpoint updates a specific news item.
- **Delete news item** `DELETE /news/{news_id}`: This endpoint deletes a specific news item.
- **Fetch RSS feed** `GET /news/rss/{api_key}/{start_date}/{end_date}`: This endpoint fetches news from an RSS feed given a specific date range.
- **Fetch GNews articles** `GET /news/gnews/{api_key}/{query}/{lang}/{country}/{max_results}`: This endpoint fetches news from GNews based on a specific query.
- **Fetch feed entries** `GET /news/entries/{source}/{limit}`: This endpoint fetches a limited number of news entries from a specified source.

## Companies

- **Create company** `POST /company`: This endpoint creates a new company.
- **Get all companies** `GET /company`: This endpoint retrieves all companies.
- **Get company by ticker** `GET /company/{ticker}`: This endpoint retrieves a specific company using its ticker.

## Articles

- **Create article** `POST /articles`: This endpoint creates a new article.
- **Get all articles** `GET /articles`: This endpoint retrieves all articles.
- **Get article** `GET /articles/{article_id}`: This endpoint retrieves a specific article using its ID.
- **Delete article** `DELETE /articles/{article_id}`: This endpoint deletes a specific article.
- **Get score by article ID** `GET /articles/{article_id}/score`: This endpoint retrieves the sentiment score of a specific article.