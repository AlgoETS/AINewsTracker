# -*- coding: utf-8 -*-
from typing import List
from fastapi import APIRouter, HTTPException
from app.core.trading.strategy import execute_trading_strategy

router = APIRouter()

# Single company
@router.get("/execute_trading_strategy/{company}")
async def execute_trading_strategy_single(company: str):
    try:
        return await execute_trading_strategy([company])
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e

# Multiple companies
@router.post("/execute_trading_strategy")
async def execute_trading_strategy_multiple(companies: List[str]):
    try:
        return await execute_trading_strategy(companies)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
