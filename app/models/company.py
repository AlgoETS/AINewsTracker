from pydantic import BaseModel

class Company(BaseModel):
    name: str
    ticker: str
