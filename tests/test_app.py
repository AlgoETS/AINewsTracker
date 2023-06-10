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


def test_health():
    response = client.get("/health")
    print(response.json())
    assert response.status_code == 200
    data = response.json()

    assert data["status"] == "ok"
    assert data["version"]
    assert data["uptime"]
    assert data["hostname"]
    assert data["environment"]

    dependencies = data["dependencies"]
    for dep in ["redis", "mongodb", "prometheus"]:
        assert dep in dependencies
        assert dependencies[dep]["status"] in ["ok", "unavailable"]
        assert dependencies[dep]["version"]
        assert dependencies[dep]["uptime"]
        assert dependencies[dep]["hostname"]
        assert dependencies[dep]["environment"]



def test_404_error():
    response = client.get("/nonexistent")
    assert response.status_code == 404


def test_favicon():
    response = client.get("/favicon.ico")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/x-icon"


def test_cache():  # sourcery skip: extract-duplicate-method
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "AI News Tracker API"

    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "AI News Tracker API"
