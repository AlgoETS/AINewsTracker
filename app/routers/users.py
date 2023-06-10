from fastapi import APIRouter
from .models import UserDTO
from .database import collection_users

router = APIRouter()

@router.post("/users")
def create_user(user: UserDTO):
    user_dict = user.dict()
    user_dict["_id"] = str(ObjectId())
    result = collection_users.insert_one(user_dict)
    return result.inserted_id

@router.get("/users")
def get_all_users():
    users = collection_users.find()
    return [UserDTO(**user) for user in users]

@router.get("/users/{user_id}")
def get_user(user_id: str):
    user = collection_users.find_one({"_id": user_id})
    return UserDTO(**user)

@router.put("/users/{user_id}")
def update_user(user_id: str, updated_user: UserDTO):
    updated_user_dict = updated_user.dict()
    collection_users.update_one({"_id": user_id}, {"$set": updated_user_dict})
    return {"message": "User updated successfully"}

@router.delete("/users/{user_id}")
def delete_user(user_id: str):
    collection_users.delete_one({"_id": user_id})
    return {"message": "User deleted successfully"}
