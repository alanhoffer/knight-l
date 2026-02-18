"""Tests de la base de datos."""

import os

import pytest
from sqlalchemy import text

# SQLite en memoria para tests
os.environ["DATABASE_URL"] = "sqlite:///:memory:"


def test_engine_creates_with_sqlite():
    """Engine debe crearse correctamente con SQLite."""
    from app.infrastructure.database.base import engine

    # Conectarse sin error
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        assert result.scalar() == 1


def test_base_exists():
    """Base declarativa debe existir."""
    from app.infrastructure.database.base import Base

    assert Base is not None
    assert hasattr(Base, "metadata")
