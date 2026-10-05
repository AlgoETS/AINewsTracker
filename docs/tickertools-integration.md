# TickerTools Integration Contract

AINewsTracker is the upstream service for financial-news ingestion, FinBERT
enrichment, and article persistence. TickerTools consumes the enriched article
feed to calculate its S&P 500 ticker, sector, and market daily mood metrics.

## Article Feed

The versioned integration endpoint is:

```http
GET /v1/articles?symbols=AAPL,MSFT&from=2026-10-02T20:00:00Z&to=2026-10-03T20:00:00Z&limit=500&cursor=<opaque>
Authorization: Bearer <service-credential>
```

Parameters:

- `symbols`: optional comma-separated normalized ticker symbols.
- `from`: inclusive RFC 3339 timestamp in UTC.
- `to`: exclusive RFC 3339 timestamp in UTC.
- `limit`: page size, from 1 through 500.
- `cursor`: opaque continuation token that preserves filters and ordering.

Results are ordered ascending by `publishedAt`, then `articleId`. A response
contains `nextCursor`, or `null` when no additional page exists.

## Article Shape

Every returned article must provide the following fields:

```json
{
  "articleId": "immutable-article-id",
  "url": "https://publisher.example/article",
  "publishedAt": "2026-10-02T20:00:00Z",
  "ingestedAt": "2026-10-02T20:02:15Z",
  "source": "publisher.example",
  "tickers": ["AAPL"],
  "sentimentLabel": "positive",
  "sentimentProbabilities": {
    "positive": 0.78,
    "negative": 0.04,
    "neutral": 0.18
  },
  "modelName": "ProsusAI/finbert",
  "modelVersion": "configured-version",
  "summary": "Optional summary"
}
```

`sentimentProbabilities` values must sum to approximately `1.0`. Raw article
text is intentionally excluded from this integration feed.

## Error And Availability Expectations

- Invalid filters or cursors return `400`.
- Missing or invalid service credentials return `401`.
- Rate limiting returns `429` with `Retry-After`.
- Transient service failures return `5xx` with `Retry-After` when retryable.
- TickerTools retries `429` and transient `5xx` responses with exponential
  backoff.

AINewsTracker must make the complete agreed ticker-universe feed available
within 15 minutes of a market-session close. TickerTools owns the versioned
S&P 500 constituent universe and sector mapping; AINewsTracker treats the
current symbols as ingestion input.