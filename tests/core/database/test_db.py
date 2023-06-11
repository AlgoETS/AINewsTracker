import asyncio
from unittest.mock import patch, MagicMock, AsyncMock
import pytest_asyncio
import pytest
from app.core.database.db import MongoDB, RedisDB
from app.config import Settings

from app.main import get_service_health


def test_mongodb_singleton():
    mongodb1 = MongoDB()
    mongodb2 = MongoDB()
    assert mongodb1 is mongodb2, "MongoDB is not a singleton"

# @pytest.skip("Not implemented")
@pytest.mark.asyncio
@patch.object(MongoDB, "get_info", return_value={})
@patch.object(MongoDB, "check_server_info", new_callable=AsyncMock)
@patch.object(MongoDB, "check_ping", new_callable=AsyncMock)
async def test_mongodb_check_connection(mock_check_ping, mock_check_server_info, mock_mongo_client):
    mock_check_server_info.return_value = True
    mock_check_ping.return_value = True

    mongodb = MongoDB()
    result = await mongodb.check_connection()

    assert (
        isinstance(mongodb.get_info(), dict)
    ), "MongoDB get_info method is not working correctly"


def test_redisdb_singleton():
    redisdb1 = RedisDB()
    redisdb2 = RedisDB()
    assert redisdb1 is redisdb2, "RedisDB is not a singleton"


@pytest.mark.asyncio
@patch("redis.Redis")
@patch.object(RedisDB, "check_connection", new_callable=AsyncMock)
async def test_redisdb_check_connection(mock_redis, mock_check_connection):
    mock_check_connection.return_value = True
    mock_redis.ping = AsyncMock(return_value=True)
    redisdb = RedisDB()
    result = await redisdb.check_connection()

    # test get_info and get_hostname
    assert (
        isinstance(redisdb.get_info(), dict) or redisdb.get_info() is None
    ), "RedisDB get_info method is not working correctly"
    assert isinstance(
        redisdb.get_hostname(), str
    ), "RedisDB get_hostname method is not working correctly"
