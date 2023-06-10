from pymongo import MongoClient
from dotenv import load_dotenv
from pydantic import BaseModel
from datetime import datetime
from typing import List
import os

# load env variables
load_dotenv()

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["AINewsTracker"]
collection_names = ["companies", "articles", "scores", "rss_feeds"]
collections = {name: db[name] for name in collection_names}


