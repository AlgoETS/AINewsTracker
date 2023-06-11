import os
from pymongo import MongoClient
import redis
from app.config import Settings
import asyncio
from concurrent.futures import ThreadPoolExecutor

env_file = os.getenv("ENV_FILE") if "ENV_FILE" in os.environ else "../../../.env"

settings = Settings(env_file)


class MongoDB:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            # Connect to MongoDB
            cls._instance._client = MongoClient(settings.MONGODB_URL)
            cls._instance._db = cls._instance._client["AINewsTracker"]
            cls._instance.create_collections(["companies", "articles", "news_feed", "users"])
        return cls._instance

    def create_collections(self, collection_names):
        self._collections = {name: self._db[name] for name in collection_names}

    def get_collection(self, collection_name):
        return self._collections.get(collection_name, None)

    async def check_server_info(self):
        loop = asyncio.get_event_loop()
        with ThreadPoolExecutor() as pool:
            result = await loop.run_in_executor(pool, self._client.server_info)
        return result

    async def check_ping(self):
        loop = asyncio.get_event_loop()
        with ThreadPoolExecutor() as pool:
            result = await loop.run_in_executor(pool, self._client.admin.command, "ping")
        return result

    async def check_connection(self):
        try:
            await asyncio.wait_for(self.check_server_info(), timeout=5)
            await asyncio.wait_for(self.check_ping(), timeout=5)
            return True
        except asyncio.TimeoutError:
            print("Connection check exceeded timeout")
            return False
        except Exception as e:
            print(f"Connection failed with error: {str(e)}")
            return False

    def get_info(self):
        return self._client.server_info() if self._client else None

    def get_client(self):
        return self._client or None

    def close(self):
        self._client.close()


class RedisDB:
    _instance = None

    def __new__(cls, host="localhost", port=6379, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            try:
                cls._instance._connection = redis.Redis(
                    host=settings.REDIS_HOST,
                    port=settings.REDIS_PORT,
                    password=settings.REDIS_PASSWORD,
                )
                cls._instance._connection.ping()
                print("Connected to Redis")
            except redis.ConnectionError:
                print("Redis server not available")
                cls._instance._connection = None
        return cls._instance

    async def check_connection(self):
        try:
            await asyncio.wait_for(self._connection.ping(), timeout=5)
            return True
        except asyncio.TimeoutError:
            print("Connection check exceeded timeout")
            return False
        except Exception as e:
            print(f"Connection failed with error: {str(e)}")
            return False


    def get_info(self):
        return self._connection.info() if self._connection else None

    def get_connection(self):
        return self._connection

    def get_hostname(self):
        if self._connection is None:
            return "unknown"
        return self._connection.connection_pool.connection_kwargs["host"]

