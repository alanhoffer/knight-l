"""Tests del endpoint principal y app FastAPI."""

import pytest


def test_root_returns_app_info(client):
    """GET / debe devolver nombre y versión de la app."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "app" in data
    assert "version" in data
    assert data["app"] == "IronClash Backend"
    assert data["version"] == "1.0.0"


def test_root_returns_json(client):
    """GET / debe devolver JSON."""
    response = client.get("/")
    assert response.headers["content-type"] == "application/json"
