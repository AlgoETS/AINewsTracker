# -*- coding: utf-8 -*-
import os
from typing import Optional

from dotenv import load_dotenv


class Settings:
    """Class to hold all environment settings."""

    _instance = None
    default_env_file = ".env"  # Set the default env_file path here


    def __new__(cls, env_file: Optional[str] = None, env: Optional[dict] = None):
        if cls._instance is None:
            cls._instance = super(Settings, cls).__new__(cls)
            cls._instance.__initiated = False
        return cls._instance

    def __init__(self, env_file: Optional[str] = None, env: Optional[dict] = None):
        if self.__initiated:
            return
        self.__initiated = True
        if env is None:
            self.env = os.environ
            if env_file is None:
                env_file = self.default_env_file  # Set the default env_file path if not provided
            load_dotenv(dotenv_path=env_file, verbose=True)
        else:
            self.env = env

        self.ENVIRONMENT = self.get_env_variable("ENVIRONMENT", "dev")
        self.HOST = self.get_env_variable("HOST", "0.0.0.0")
        self.PORT = int(self.get_env_variable("PORT", 8000))
        self.RELOAD = bool(self.get_env_variable("RELOAD", True))
        self.PROMETHEUS_PORT = int(self.get_env_variable("PROMETHEUS_PORT", 8000))

        self.SECRET_KEY = self.get_env_variable(
            "SECRET_KEY",
            "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7",
        )
        self.ALGORITHM = self.get_env_variable("ALGORITHM", "HS256")
        self.ACCESS_TOKEN_EXPIRE_MINUTES = int(
            self.get_env_variable("ACCESS_TOKEN_EXPIRE_MINUTES", 60 * 24 * 7)
        )

        self.REDIS_HOST = self.get_env_variable("REDIS_HOST", "localhost")
        self.REDIS_PASSWORD = self.get_env_variable("REDIS_PASSWORD", "")
        self.REDIS_PORT = self.get_env_variable("REDIS_PORT", 6379)
        self.REDIS_DB = self.get_env_variable("REDIS_DB", "AlgoETS-free-db")
        self.REDIS_USERNAME = self.get_env_variable("REDIS_USERNAME", "")

        self.FMP_API_KEY = self.get_env_variable("FMP_API_KEY")
        self.NEWS_API= self.get_env_variable("NEWS_API")
        self.BINANCE_API_KEY = self.get_env_variable("BINANCE_API_KEY")
        self.SECRET_KEY_BINANCE = self.get_env_variable("SECRET_KEY_BINANCE")
        self.IEX_TOKEN = self.get_env_variable("IEX_TOKEN")
        self.FINNHUB_TOKEN = self.get_env_variable("FINNHUB_TOKEN")

        self.BASE_URL_FMP = self.get_env_variable(
            "BASE_URL_FMP", "https://financialmodelingprep.com/api/v3"
        )
        self.BASE_URL_FMP_V3 = self.get_env_variable(
            "BASE_URL_FMP_V3", "https://financialmodelingprep.com/api/v3"
        )
        self.BASE_URL_FMP_V4 = self.get_env_variable(
            "BASE_URL_FMP_V4", "https://financialmodelingprep.com/api/v4"
        )

        self.BASE_URL_BINANCE = self.get_env_variable(
            "BASE_URL_BINANCE", "https://api.binance.com"
        )

        self.BASE_IEXCLOUD_URL = self.get_env_variable(
            "BASE_IEXCLOUD_URL", "https://cloud.iexapis.com/stable"
        )

        self.BASE_FINNHUB_URL = self.get_env_variable(
            "BASE_FINNHUB_URL", "https://finnhub.io/api/v1"
        )

        self.BASE_URL_QUANDL = self.get_env_variable(
            "BASE_URL_QUANDL", "https://www.quandl.com/api/v3"
        )

        # TWITTER
        self.TWTTER_CONSUMER_KEY = self.get_env_variable("TWTTER_CONSUMER_KEY")
        self.TWITTER_CONSUMER_SECRET = self.get_env_variable("TWITTER_CONSUMER_SECRET")
        self.TWITTER_ACCESS_TOKEN = self.get_env_variable("TWITTER_ACCESS_TOKEN")
        self.TWITTER_BEARER_TOKEN = self.get_env_variable("TWITTER_BEARER_TOKEN")

        # OPENBB
        self.FRED_KEY = self.get_env_variable("FRED_KEY")
        self.QUANDL_KEY = self.get_env_variable("QUANDL_KEY")
        self.ALPHAVANTAGE = self.get_env_variable("ALPHAVANTAGE")

        # MongDB
        self.MONGODB_URL = self.get_env_variable(
            "MONGODB_URL", "mongodb://mongo:mongo@localhost:27017/"
        )

    def get_env_variable(
        self, var_name: str, default: Optional[str] = None
    ) -> Optional[str]:
        """Get environment variable value or return None if not found."""
        if var_value := self.env.get(var_name):
            return var_value
        if default is not None:
            return default
        print(f"Warning: {var_name} environment variable not set.")
        return None

    @classmethod
    def reset(cls):
        cls._instance = None
