from pydantic import BaseModel
from bson import ObjectId
from .models import Company
from .database import collection_companies
router = APIRouter()

@router.post("/companies")
def create_company(company: Company):
    company_dict = company.dict()
    company_dict["_id"] = str(ObjectId())
    result = collection_companies.insert_one(company_dict)
    return result.inserted_id

@router.get("/companies")
def get_all_companies():
    companies = collection_companies.find()
    return [Company(**company) for company in companies]

@router.get("/companies/{ticker}")
def get_company_by_ticker(ticker: str):
    company = collection_companies.find_one({"ticker": ticker})
    return Company(**company) if company else None