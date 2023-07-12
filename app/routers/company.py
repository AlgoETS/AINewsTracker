# -*- coding: utf-8 -*-
import logging
from fastapi import APIRouter, HTTPException
from app.core.logging import Logger
from typing import List


logger = Logger(logging.INFO).get_logger()

from app.core.repo.company import (
    create_company,
    get_all_companies,
    get_company_by_ticker,
)
from app.models import Company

router = APIRouter(
    prefix="/company",
    tags=["Company"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", status_code=201)
async def create_company_handler(company: Company):
    company_id = await create_company(company)
    logger.info(f"Company {company_id} created successfully")
    return {"message": "Company created successfully", "company_id": company_id}

@router.get("/", response_model=List[Company])
async def get_all_companies_handler():
    logger.info("Fetching all companies")
    return await get_all_companies()

@router.get("/{ticker}", response_model=Company)
async def get_company_by_ticker_handler(ticker: str):
    if company := await get_company_by_ticker(ticker):
        logger.info(f"Company {ticker} fetched successfully")
        return company
    else:
        logger.error(f"Company {ticker} not found")
        raise HTTPException(status_code=404, detail="Company not found")
