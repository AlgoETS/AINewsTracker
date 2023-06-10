import os
from pymongo import MongoClient
import redis
from app.config import Settings


env_file = os.getenv("ENV_FILE") if "ENV_FILE" in os.environ else ".env"

settings = Settings(env_file)


class MongoDB:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            # Connect to MongoDB
            cls._instance._client = MongoClient(settings.MONGODB_URL)
            cls._instance._db = cls._instance._client["AINewsTracker"]
            cls._instance.create_collections(["companies", "articles", "news_feed"])
        return cls._instance

    def create_collections(self, collection_names):
        self._collections = {name: self._db[name] for name in collection_names}

    def get_collection(self, collection_name):
        return self._collections.get(collection_name, None)

    def check_connection(self):
        try:
            self._client.server_info()
            self._client.admin.command('ping')
            return True
        except Exception:
            return False

    def get_info(self):
        return self._client.server_info()

    def get_client(self):
        return self._client

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
                    password=settings.REDIS_PASSWORD
                )
                cls._instance._connection.ping()
                print("Connected to Redis")
            except redis.ConnectionError:
                print("Redis server not available")
                cls._instance._connection = None
        return cls._instance

    def check_connection(self):
        try:
            self._connection.ping()
            return True
        except Exception:
            return False

    def get_info(self):
        return self._connection.info() if self._connection else None

    def get_connection(self):
        return self._connection

    def get_hostname(self):
        return self._connection.connection_pool.connection_kwargs["host"]
