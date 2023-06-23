# -*- coding: utf-8 -*-
from datetime import datetime, timedelta, timezone
from typing import Optional

from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from passlib.context import CryptContext
from pydantic import BaseModel

from app.core.database import MongoDB
from app.config import Settings
import os

env_file = os.getenv("ENV_FILE") if "ENV_FILE" in os.environ else "../../../.env"
settings = Settings(env_file)

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

class AuthService:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    @staticmethod
    def get_password_hash(password: str):
        return AuthService.pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password, hashed_password):
        return AuthService.pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode["exp"] = expire
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    @staticmethod
    def authenticate_user(email: str, password: str):
        user = MongoDB().get_collection("users").find_one({"email": email})
        if user and AuthService.verify_password(password, user.get("password", "")):
            return user
        return None
