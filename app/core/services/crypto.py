# -*- coding: utf-8 -*-
from enum import Enum
from typing import List
from app.config import Settings
from app.core.services import make_api_request


settings = Settings()

FMP_API_KEY = settings.FMP_API_KEY
BASE_URL_FMP = settings.BASE_URL_FMP

class CryptoSymbol(Enum):
    BTCUSD = "BTCUSD"
    ETHUSD = "ETHUSD"
    LTCUSD = "LTCUSD"
    BCHUSD = "BCHUSD"
    XRPUSD = "XRPUSD"
    EOSUSD = "EOSUSD"
    XLMUSD = "XLMUSD"
    TRXUSD = "TRXUSD"
    ETCUSD = "ETCUSD"
    DASHUSD = "DASHUSD"
    ZECUSD = "ZECUSD"
    XTZUSD = "XTZUSD"
    XMRUSD = "XMRUSD"
    ADAUSD = "ADAUSD"
    NEOUSD = "NEOUSD"
    XEMUSD = "XEMUSD"
    VETUSD = "VETUSD"
    DOGEUSD = "DOGEUSD"
    OMGUSD = "OMGUSD"
    ZRXUSD = "ZRXUSD"
    BATUSD = "BATUSD"
    USDTUSD = "USDTUSD"
    LINKUSD = "LINKUSD"
    BTTUSD = "BTTUSD"
    BNBUSD = "BNBUSD"


def get_historical_price_full_crypto(symbol: CryptoSymbol):
    api_endpoint = f"{BASE_URL_FMP}/historical-price-full/crypto/{symbol.value}"
    params = {"apikey": FMP_API_KEY}
    return make_api_request(api_endpoint, params)


def get_all_crypto() -> List[CryptoSymbol]:
    return list(CryptoSymbol)
