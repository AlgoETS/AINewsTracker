# -*- coding: utf-8 -*-
from bson import ObjectId

from app.core.database import MongoDB
from app.models.company import Company


def create_company(company: Company):
    company_dict = company.dict()
    company_dict["_id"] = str(ObjectId())  # Convert ObjectId to a string
    result = MongoDB().get_collection("companies").insert_one(company_dict)
    return result.inserted_id

def create_companies(companies: list[Company]):
    company_dicts = [company.dict() for company in companies]
    for company_dict in company_dicts:
        company_dict["_id"] = str(ObjectId())  # Convert ObjectId to a string
    result = MongoDB().get_collection("companies").insert_many(company_dicts)
    return result.inserted_ids


def get_all_companies() -> list[Company]:
    companies = MongoDB().get_collection("companies").find()
    return [Company(**company) for company in companies]


def get_company_by_ticker(ticker: str) -> Company:
    company = MongoDB().get_collection("companies").find_one({"ticker": ticker})
    return Company(**company) if company else None
