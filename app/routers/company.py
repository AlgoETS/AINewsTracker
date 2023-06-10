# -*- coding: utf-8 -*-
from fastapi import APIRouter, HTTPException

from app.core.repo.company import (
    create_company,
    get_all_companies,
    get_company_by_ticker,
)
from app.models import Company

router = APIRouter(
    prefix="/companies",
    tags=["companies"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", status_code=201)
def create_company_handler(company: Company):
    company_id = create_company(company)
    return {"message": "Company created successfully", "company_id": company_id}


@router.get("/", response_model=list[Company])
def get_all_companies_handler():
    return get_all_companies()


@router.get("/{ticker}", response_model=Company)
def get_company_by_ticker_handler(ticker: str):
    if company := get_company_by_ticker(ticker):
        return company
    else:
        raise HTTPException(status_code=404, detail="Company not found")
