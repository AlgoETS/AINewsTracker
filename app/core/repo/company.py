from typing import Optional, List
from bson.objectid import ObjectId

from app.core.database import MongoDB
from app.models.company import Company
from typing import Optional, List

from app.core.logging import Logger
import logging

logger = Logger(logging.INFO).get_logger()

mongo_db = MongoDB()
collection = mongo_db.get_collection("companies")

async def create_company(company: Company):
    logger.info("Creating company")
    company_dict = company.dict()
    company_dict["_id"] = str(ObjectId())
    result = await collection.insert_one(company_dict)
    return result.inserted_id

async def create_companies(companies: List[Company]):
    logger.info("Creating companies")
    companies = [dict(item.dict()) for item in companies]
    inserted_ids = []
    for company in companies:
        filter_query = {"symbol": company["symbol"]}  # filter condition for the upsert
        update_query = {"$set": company}  # update operation

        # upsert operation
        result = await collection.update_one(filter_query, update_query, upsert=True)

        # If a new document was inserted, retrieve the inserted ID
        if result.upserted_id:
            inserted_ids.append(result.upserted_id)

    return inserted_ids

async def get_all_companies() -> List[Company]:
    logger.info("Fetching all companies")
    companies = await collection.find().to_list(length=100)  # specify max limit here
    return [Company(**company) for company in companies]

async def get_company_by_ticker(ticker: str) -> Optional[Company]:
    logger.info(f"Fetching company {ticker}")
    company = await collection.find_one({"ticker": ticker})
    return Company(**company) if company else None

