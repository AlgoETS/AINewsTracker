from datetime import date, datetime
from pydantic import BaseModel
from typing import List
from ..database.db import collection_users
from bson import ObjectId
from beanie import Document

class UserDTO(BaseModel):
    name: str

class Client(Document):
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

def create_user(user: UserDTO):
    user_dict = user.dict()
    user_dict["_id"] = str(ObjectId())  # Convert ObjectId to a string
    result = collection_users.insert_one(user_dict)
    return result.inserted_id

def get_user(user_id: str) -> UserDTO:
    user = collection_users.find_one({"_id": user_id})
    return UserDTO(**user)

def get_all_users() -> List[UserDTO]:
    users = collection_users.find()
    return [UserDTO(**user) for user in users]

def update_user(user_id: str, updated_user: UserDTO):
    updated_user_dict = updated_user.dict()
    collection_users.update_one({"_id": user_id}, {"$set": updated_user_dict})

def delete_user(user_id: str):
    collection_users.delete_one({"_id": user_id})