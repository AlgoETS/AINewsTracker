# -*- coding: utf-8 -*-
from typing import Optional

from pydantic import BaseModel


class Company(BaseModel):
    id: Optional[str]
    name: str
    ticker: str
    description: str
    website: str
    industry: str
    sector: str
    country: str
