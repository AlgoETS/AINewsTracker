from fastapi import APIRouter, HTTPException
from typing import List
from ..models.users import UserDTO, create_user, get_user, get_all_users, update_user, delete_user

# init router
router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

# User routes
@router.post("/", status_code=201)
def create_user_handler(user: UserDTO):
    user_id = create_user(user)
    return {"message": "User created successfully", "user_id": user_id}

@router.get("/{user_id}", response_model=UserDTO)
def get_user_handler(user_id: str):
    user = get_user(user_id)
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")

@router.get("/", response_model=List[UserDTO])
def get_all_users_handler():
    return get_all_users()

@router.put("/{user_id}")
def update_user_handler(user_id: str, updated_user: UserDTO):
    update_user(user_id, updated_user)
    return {"message": "User updated successfully"}

@router.delete("/{user_id}")
def delete_user_handler(user_id: str):
    delete_user(user_id)
    return {"message": "User deleted successfully"}