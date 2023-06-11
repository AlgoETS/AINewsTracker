# -*- coding: utf-8 -*-
import pytest
from fastapi.testclient import TestClient
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend

from app.main import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def prepare():
    FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")


def test_read_root():
    client.__init__(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "AI News Tracker API"


def test_404_error():
    response = client.get("/nonexistent")
    assert response.status_code == 404


def test_favicon():
    response = client.get("/favicon.ico")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/x-icon"


def test_cache():  # sourcery skip: extract-duplicate-method
    response_1 = client.get("/")
    assert response_1.status_code == 200
    data_1 = response_1.json()
    assert data_1 == "AI News Tracker API"

    response_2 = client.get("/")
    assert response_2.status_code == 200
    data_2 = response_2.json()

    assert data_1 == data_2
