"""Pytest fixtures compartidos."""

import os

import pytest
from fastapi.testclient import TestClient

# Usar SQLite en memoria para tests (rápido, aislado)
os.environ["DATABASE_URL"] = "sqlite:///:memory:"
os.environ["REDIS_URL"] = "redis://localhost:6379/1"  # DB 1 para no mezclar con dev


@pytest.fixture(autouse=True)
def create_tables():
    """Crear tablas antes de cada test (usa modelos, no migraciones)."""
    from app.infrastructure.database.base import Base, engine

    # Importar modelos para que se registren en Base.metadata
    from app.infrastructure.database.models import (  # noqa: F401
        User, Character, Map, GearTemplate, CharacterGear,
        LootTable, LootTableEntry, Enemy, MapInstance, EnemyInstance,
        Battle, BattleLoot, BattleSnapshot,
    )

    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client() -> TestClient:
    """Cliente de test para la API."""
    from app.main import app
    return TestClient(app)
