# -*- coding: utf-8 -*-
from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.core.repo.user import get_current_user
from app.models import UserDTO, Token, UserCreate
from app.core.logging import Logger
from app.core.services.user import ACCESS_TOKEN_EXPIRE_MINUTES, AuthService
from app.core.repo.user import get_user_by_email, insert_new_user
import logging

logger = Logger(logging.INFO).get_logger()

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)


@router.post("/signup", response_model=UserDTO)
async def create_user(user: UserCreate):
    if get_user_by_email(user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered"
        )
    return insert_new_user(user.dict())


@router.post("/login", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = AuthService.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = AuthService.create_access_token(
        data={"sub": user.get("email")}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
