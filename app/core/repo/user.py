from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from app.config import Settings

from app.core.database import MongoDB
from app.models.users import UserDTO

settings = Settings()

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

mongo_db = MongoDB()
user_collection = mongo_db.get_collection("users")

class TokenData(BaseModel):
    email: Optional[str] = None

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


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


def get_user(email: str) -> Optional[UserDTO]:
    if user := user_collection.find_one({"email": email}):
        return UserDTO(**user)
    return None

def get_user_by_email(email: str):
        return MongoDB().get_collection("users").find_one({"email": email})
