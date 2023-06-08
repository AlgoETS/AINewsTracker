# -*- coding: utf-8 -*-
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_root():
    client.__init__(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "AI News Tracker API"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "pass"