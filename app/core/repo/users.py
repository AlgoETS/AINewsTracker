# -*- coding: utf-8 -*-
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

from app.core.database import MongoDB
from app.models.users import UserDTO

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Use email instead of username
class TokenData(BaseModel):
    email: Optional[str] = None


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# Use email as identifier
def authenticate_user(email: str, password: str):
    if user := get_user(email):
        return user if verify_password(password, user.password) else False
    else:
        return False


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError as e:
        raise credentials_exception from e
    user = get_user(token_data.email)
    if user is None:
        raise credentials_exception
    return user


# Use email as identifier
def get_user(email: str) -> UserDTO:
    user = MongoDB().get_collection("users").find_one({"email": email})
    return UserDTO(**user)
