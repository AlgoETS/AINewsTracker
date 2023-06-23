# -*- coding: utf-8 -*-
from typing import Optional

from pydantic import BaseModel

class Company(BaseModel):
    symbol: str
    name: str
    sector: str
    subSector: str
    headQuarter: str
    dateFirstAdded: str
    cik: str
    founded: str
