"""Tests para el endpoint de health check."""

import pytest


def test_health_returns_200(client):
    """GET /health debe devolver 200."""
    response = client.get("/health")
    assert response.status_code == 200


def test_health_returns_status(client):
    """GET /health debe incluir status y checks."""
    response = client.get("/health")
    data = response.json()
    assert "status" in data
    assert data["status"] in ("healthy", "unhealthy")
    assert "checks" in data
    assert "database" in data["checks"]
    assert data["checks"]["database"] == "ok"


def test_health_includes_app_info(client):
    """GET /health debe incluir app y version."""
    response = client.get("/health")
    data = response.json()
    assert data["app"] == "IronClash Backend"
    assert data["version"] == "1.0.0"
