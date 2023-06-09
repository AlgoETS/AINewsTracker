# -*- coding: utf-8 -*-
import os

from dotenv import load_dotenv

load_dotenv(
    dotenv_path=os.path.join(os.path.dirname(__file__), "../.env.default"),
    verbose=True,
)


SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
REDIS_PORT = os.getenv("REDIS_PORT")

FMP_API_KEY = os.getenv("FMP_API_KEY")
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
SECRET_KEY_BINANCE = os.getenv("SECRET_KEY_BINANCE")
IEX_TOKEN = os.getenv("IEX_TOKEN")
FINNHUB_TOKEN = os.getenv("FINNHUB_TOKEN")

BASE_URL_FMP = "https://financialmodelingprep.com/api/v3"
BASE_URL_FMP_V3 = "https://financialmodelingprep.com/api/v3"
BASE_URL_FMP_V4 = "https://financialmodelingprep.com/api/v4"

BASE_URL_BINANCE = "https://api.binance.com"

BASE_IEXCLOUD_URL = "https://cloud.iexapis.com/stable"

BASE_FINNHUB_URL = "https://finnhub.io/api/v1"

BASE_URL_QUANDL = "https://www.quandl.com/api/v3"

# TWITTER
TWTTER_CONSUMER_KEY = ""
TWITTER_CONSUMER_SECRET = ""
TWITTER_ACCESS_TOKEN = ""
TWITTER_BEARER_TOKEN = ""

# OPENBB
FRED_KEY = ""
QUANDL_KEY = ""
ALPHAVANTAGE = ""

# MongDB
MONGODB_URL = os.getenv("MONGODB_URL")