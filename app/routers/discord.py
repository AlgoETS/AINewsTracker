# -*- coding: utf-8 -*-
import logging
from fastapi import APIRouter, HTTPException, Request
from app.core.logging import Logger

logger = Logger(logging.INFO).get_logger()

from app.core.services.discord import send_message
from app.models import Article

router = APIRouter(
    prefix="/discord",
    tags=["Discord"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
def send_message_handler(message: str):
    article_id = send_message(str)
    logger.info(f"Article {article_id} created successfully")
    return {"message": "Message sent successfully", "article_id": article_id}

