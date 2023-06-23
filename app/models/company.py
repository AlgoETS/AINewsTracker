# -*- coding: utf-8 -*-
from typing import Optional

from pydantic import BaseModel
{'symbol': 'MMM', 'name': '3M', 'sector': 'Industrials', 'subSector': 'Industrial Conglomerates',
  'headQuarter': 'Saint Paul, Minnesota', 'dateFirstAdded': '1957-03-04', 'cik': '0000066740', 'founded': '1902'}

class Company(BaseModel):
    id: Optional[str]
    symbol: str
    name: str
    sector: str
    subSector: str
    headQuarter: str
    dateFirstAdded: str
    cik: str
    founded: str
