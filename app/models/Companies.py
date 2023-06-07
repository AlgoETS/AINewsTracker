from pydantic import BaseModel

class Companies(BaseModel):
    name: str
    ticker: str
