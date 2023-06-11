# -*- coding: utf-8 -*-
from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel

class UserDTO(BaseModel):
    email: Optional[str] = None

class User(BaseModel):
    id: Optional[str]
    last_name: str
    first_name: str
    email: str
    phone: str
    birthday: date
    address: str
    city: str
    province: str
    postal_code: str
    password: str
    plan: str
    credit_id: int
    points: int
    balance: float
    friends: list[int] = []
    last_login: date
    last_logout: datetime

