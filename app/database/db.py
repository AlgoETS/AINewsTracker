from pymongo import MongoClient
from dotenv import load_dotenv
import os

# load env variables
load_dotenv()

# Connect to MongoDB
client = MongoClient(os.getenv("Password"))

# database
db = client['AI_News_Tracker']

# gettting collection
collection_users = db['users']
collection_company = db['company']
collection_news = db['news']
collection_news_sentiment = db['news_sentiment']
collection_news_sentiment_score = db['news_sentiment_score']


