from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel


class UserDTO(BaseModel):
    name : str
class User(BaseModel):
    id: Optional[str]
    nom_famille: str
    prenom: str
    courriel: str
    telephone: str
    anniversaire: date
    adresse: str
    ville: str
    province: str
    code_postal: str
    password: str
    forfait: str
    credit_id: int
    points: int
    solde: float
    friends: list[int] = []
    last_login: date
    last_logout: datetime