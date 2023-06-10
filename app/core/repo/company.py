
from app.models.company import Company
from app.core.database import MongoDB
from bson import ObjectId


def create_company(company: Company):
    company_dict = company.dict()
    company_dict["_id"] = str(ObjectId())  # Convert ObjectId to a string
    result = MongoDB().get_collection("companies").insert_one(company_dict)
    return result.inserted_id

def get_all_companies() -> list[Company]:
    companies = MongoDB().get_collection("companies").find()
    return [Company(**company) for company in companies]

def get_company_by_ticker(ticker: str) -> Company:
    company = MongoDB().get_collection("companies").find_one({"ticker": ticker})
    return Company(**company) if company else None

