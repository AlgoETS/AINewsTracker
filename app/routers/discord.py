# -*- coding: utf-8 -*-
import logging
from fastapi import APIRouter, HTTPException, Request
from app.core.logging import Logger

logger = Logger(logging.INFO).get_logger()

from app.core.services.discord import send_message


router = APIRouter(
    prefix="/discord",
    tags=["Discord"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def send_message_handler(message: str):
    await  send_message(message)
    logger.info("Message  sent successfully")
    return {"message": "Message sent successfully"}

