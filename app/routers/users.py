# -*- coding: utf-8 -*-
from fastapi import APIRouter

# init router
router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)
