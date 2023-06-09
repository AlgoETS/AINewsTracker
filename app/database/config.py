# -*- coding: utf-8 -*-
# Load .env file
import os

from dotenv import load_dotenv

load_dotenv()

mongo_host = os.getenv("MONGO_HOST")
mongo_port = os.getenv("MONGO_PORT")
mongo_user = os.getenv("MONGO_USER")
mongo_password = os.getenv("MONGO_PASSWORD")
mongo_db = os.getenv("MONGO_DB")

redis_host = os.getenv("REDIS_HOST")
redis_password = os.getenv("REDIS_PASSWORD")
redis_port = os.getenv("REDIS_PORT")
