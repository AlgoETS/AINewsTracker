# -*- coding: utf-8 -*-
import base64
import hmac
import json
from datetime import datetime, timezone
from typing import Optional, Tuple

from fastapi import APIRouter, Header, HTTPException, Query

from app.config import Settings
from app.core.repo.article import get_articles_for_integration
from app.models.article import Article

router = APIRouter(prefix="/v1", tags=["Integration"])
settings = Settings()


def _as_utc(value: datetime) -> datetime:
    if value.tzinfo is None:
        raise ValueError("timestamps must include a UTC offset")
    return value.astimezone(timezone.utc)


def encode_cursor(article: Article) -> str:
    if article.published_at is None or article.article_id is None:
        raise ValueError("article is missing pagination fields")
    payload = {
        "publishedAt": _as_utc(article.published_at).isoformat(),
        "articleId": article.article_id,
    }
    return base64.urlsafe_b64encode(json.dumps(payload).encode()).decode().rstrip("=")


def decode_cursor(cursor: str) -> Tuple[datetime, str]:
    try:
        padded_cursor = cursor + "=" * (-len(cursor) % 4)
        payload = json.loads(base64.urlsafe_b64decode(padded_cursor).decode())
        published_at = _as_utc(datetime.fromisoformat(payload["publishedAt"]))
        article_id = payload["articleId"]
        if not isinstance(article_id, str) or not article_id:
            raise ValueError("articleId must be a non-empty string")
        return published_at, article_id
    except (KeyError, TypeError, ValueError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ValueError("invalid cursor") from error


def serialize_article(article: Article) -> dict:
    if (
        article.article_id is None
        or article.published_at is None
        or article.ingested_at is None
        or article.sentiment_probabilities is None
    ):
        raise ValueError("article is missing integration fields")
    return {
        "articleId": article.article_id,
        "url": article.url,
        "publishedAt": _as_utc(article.published_at).isoformat(),
        "ingestedAt": _as_utc(article.ingested_at).isoformat(),
        "source": article.source_name,
        "tickers": article.tickers or [],
        "sentimentLabel": article.sentiment,
        "sentimentProbabilities": article.sentiment_probabilities,
        "modelName": article.model_name or "ProsusAI/finbert",
        "modelVersion": article.model_version or "unknown",
        "summary": article.summary,
    }


async def require_service_credential(
    authorization: Optional[str] = Header(None),
) -> None:
    expected_token = settings.AINEWSTRACKER_SERVICE_TOKEN
    if not expected_token:
        raise HTTPException(status_code=503, detail="service credential is not configured")
    expected_header = f"Bearer {expected_token}"
    if authorization is None or not hmac.compare_digest(authorization, expected_header):
        raise HTTPException(status_code=401, detail="invalid service credential")


@router.get("/articles")
async def get_integration_articles(
    symbols: Optional[str] = None,
    from_time: Optional[datetime] = Query(None, alias="from"),
    to_time: Optional[datetime] = Query(None, alias="to"),
    limit: int = Query(50, ge=1, le=500),
    cursor: Optional[str] = None,
    authorization: Optional[str] = Header(None),
):
    await require_service_credential(authorization)
    try:
        normalized_from = _as_utc(from_time) if from_time else None
        normalized_to = _as_utc(to_time) if to_time else None
        if normalized_from and normalized_to and normalized_from >= normalized_to:
            raise ValueError("from must be earlier than to")
        cursor_published_at, cursor_article_id = decode_cursor(cursor) if cursor else (None, None)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error

    normalized_symbols = [symbol.strip().upper() for symbol in symbols.split(",") if symbol.strip()] if symbols else []
    articles = await get_articles_for_integration(
        normalized_symbols,
        normalized_from,
        normalized_to,
        cursor_published_at,
        cursor_article_id,
        limit,
    )
    page = articles[:limit]
    next_cursor = encode_cursor(page[-1]) if len(articles) > limit else None
    return {
        "data": [serialize_article(article) for article in page],
        "meta": {"nextCursor": next_cursor},
    }