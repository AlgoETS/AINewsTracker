from pymongo import MongoClient
from dotenv import load_dotenv
from pydantic import BaseModel
from datetime import datetime
from typing import List
import os


def connect_to_db():
    # Load environment variables
    load_dotenv()

    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["AINewsTracker"]

    return db

def create_collections(db, collection_names: List[str]):
    collection_names = ["companies", "articles", "scores", "rss_feeds"]
    collections = {name: db[name] for name in collection_names}
    return collections
