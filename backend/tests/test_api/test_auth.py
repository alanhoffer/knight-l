"""Tests for auth endpoints: register, login, me."""

import pytest


def test_register_success(client):
    """POST /api/v1/auth/register creates user and returns data without password."""
    response = client.post(
        "/api/v1/auth/register",
        json={
            "username": "testplayer",
            "email": "test@example.com",
            "password": "secret123",
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "testplayer"
    assert data["email"] == "test@example.com"
    assert "user_id" in data
    assert "password" not in data
    assert "hashed_password" not in data


def test_register_duplicate_username(client):
    """Register with existing username returns 422."""
    client.post(
        "/api/v1/auth/register",
        json={"username": "duplicate", "email": "first@example.com", "password": "secret123"},
    )
    response = client.post(
        "/api/v1/auth/register",
        json={"username": "duplicate", "email": "second@example.com", "password": "other456"},
    )
    assert response.status_code == 422
    assert "already" in response.json()["detail"].lower()


def test_register_duplicate_email(client):
    """Register with existing email returns 422."""
    client.post(
        "/api/v1/auth/register",
        json={"username": "user1", "email": "same@example.com", "password": "secret123"},
    )
    response = client.post(
        "/api/v1/auth/register",
        json={"username": "user2", "email": "same@example.com", "password": "other456"},
    )
    assert response.status_code == 422


def test_register_validation(client):
    """Register with invalid data returns 422."""
    response = client.post(
        "/api/v1/auth/register",
        json={"username": "ab", "email": "invalid", "password": "short"},
    )
    assert response.status_code == 422


def test_login_success(client):
    """POST /api/v1/auth/login returns token for valid credentials."""
    client.post(
        "/api/v1/auth/register",
        json={"username": "loginuser", "email": "login@example.com", "password": "mypass123"},
    )
    response = client.post(
        "/api/v1/auth/login",
        json={"username": "loginuser", "password": "mypass123"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
    assert data["expires_in"] > 0


def test_login_invalid_password(client):
    """Login with wrong password returns 422."""
    client.post(
        "/api/v1/auth/register",
        json={"username": "badpass", "email": "bad@example.com", "password": "correct123"},
    )
    response = client.post(
        "/api/v1/auth/login",
        json={"username": "badpass", "password": "wrongpassword"},
    )
    assert response.status_code == 422


def test_login_nonexistent_user(client):
    """Login with unknown username returns 422."""
    response = client.post(
        "/api/v1/auth/login",
        json={"username": "nobody", "password": "anything"},
    )
    assert response.status_code == 422


def test_me_requires_auth(client):
    """GET /api/v1/auth/me without token returns 401."""
    response = client.get("/api/v1/auth/me")
    assert response.status_code == 401


def test_me_returns_user(client):
    """GET /api/v1/auth/me with valid token returns user."""
    client.post(
        "/api/v1/auth/register",
        json={"username": "meuser", "email": "me@example.com", "password": "pass123"},
    )
    login_resp = client.post(
        "/api/v1/auth/login",
        json={"username": "meuser", "password": "pass123"},
    )
    token = login_resp.json()["access_token"]

    response = client.get(
        "/api/v1/auth/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "meuser"
    assert data["email"] == "me@example.com"
    assert "user_id" in data
