# -*- coding: utf-8 -*-
import asyncio
import logging
import os
from pymongo import ASCENDING
import aioredis
import contextlib
from motor.motor_asyncio import AsyncIOMotorClient

from app.config import Settings
from app.core.logging import Logger


settings = Settings()
logger = Logger(log_level=logging.DEBUG).get_logger()

class MongoDB:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._client = AsyncIOMotorClient(settings.MONGODB_URL)
            cls._instance._db = cls._instance._client["AINewsTracker"]
            cls._instance.create_collections(
                ["companies", "articles", "news_feed", "users"]
            )
        return cls._instance

    def create_collections(self, collection_names):
        self._collections = {name: self._db[name] for name in collection_names}

        # Create index on "symbol" key for the "companies" collection
        self._collections["companies"].create_index([("symbol", ASCENDING)])
        self._collections["articles"].create_index([("url", ASCENDING)])

    def get_collection(self, collection_name):
        return self._collections.get(collection_name, None)

    async def check_connection(self):
        try:
            # The command "ping" will throw an exception if cannot connect to the server
            await self._client.ping()
            return True
        except Exception as e:
            print(f"Connection failed with error: {str(e)}")
            return False

    def check_server_info(self):
        return self._client.admin.command('serverStatus')

    def check_ping(self):
        return self._client.admin.command('ping')

    def get_info(self):
        return self._client.server_info() if self._client else None

    def close(self):
        self._client.close()


class RedisDB:
    _instance = None

    def __new__(cls, host="localhost", port=6379, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._connection = None
        return cls._instance

    async def connect(self):
        if self._connection is None:
            try:
                self._connection = await aioredis.create_redis_pool(
                    f'redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}',
                    username=settings.REDIS_USERNAME,
                    password=settings.REDIS_PASSWORD,
                    db=settings.REDIS_DB,
                )
                print("Connected to Redis")
            except Exception:
                print("Redis server not available")

    async def check_connection(self):
        if self._connection is None:
            return False
        try:
            pong = await self._connection.ping()
            return pong == "PONG"
        except Exception as e:
            print(f"Connection failed with error: {str(e)}")
            return False

    def get_info(self):
        return self._connection.info() if self._connection else None

    def get_hostname(self):
        return settings.REDIS_HOST

    def close(self):
        with contextlib.suppress(Exception):
            self._connection.close()

