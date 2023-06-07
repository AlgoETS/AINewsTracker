from .database import collection_companies
from bson import ObjectId
from .models import Company

def create_company(company: Company):
    company_dict = company.dict()
    company_dict["_id"] = str(ObjectId())  # Convert ObjectId to a string
    result = collection_companies.insert_one(company_dict)
    return result.inserted_id

def get_all_companies() -> list[Company]:
    companies = collection_companies.find()
    return [Company(**company) for company in companies]

def get_company_by_ticker(ticker: str) -> Company:
    company = collection_companies.find_one({"ticker": ticker})
    return Company(**company) if company else None
