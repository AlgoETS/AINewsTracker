import os
import pytest
from unittest.mock import patch, MagicMock
from app.core.database.db import MongoDB, RedisDB
from app.config import Settings

def test_mongodb_singleton():
    mongodb1 = MongoDB()
    mongodb2 = MongoDB()
    assert mongodb1 is mongodb2, "MongoDB is not a singleton"

@patch('pymongo.MongoClient')
def test_mongodb_check_connection(mock_mongo_client):
    mock_mongo_client.server_info.return_value = True
    mock_mongo_client.admin.command.return_value = True
    mongodb = MongoDB()
    assert mongodb.check_connection() is True, "MongoDB check connection is not working correctly"

def test_redisdb_singleton():
    redisdb1 = RedisDB()
    redisdb2 = RedisDB()
    assert redisdb1 is redisdb2, "RedisDB is not a singleton"

@patch('redis.Redis')
def test_redisdb_check_connection(mock_redis):
    mock_redis.ping.return_value = True
    redisdb = RedisDB()
    assert redisdb.check_connection() is True, "RedisDB check connection is not working correctly"
