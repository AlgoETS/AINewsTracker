from pydantic import BaseModel
from typing import List
from ..database.db import collection_users
from bson import ObjectId

class UserDTO(BaseModel):
    name: str
    
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