"""Tests del esquema completo - tablas creadas correctamente."""

import os

import pytest
from sqlalchemy import text

os.environ["DATABASE_URL"] = "sqlite:///:memory:"


def test_all_tables_exist():
    """Todas las tablas del esquema deben existir tras create_all."""
    from app.infrastructure.database.base import Base, engine
    from app.infrastructure.database.models import (
        User, Character, Map, GearTemplate, CharacterGear,
        LootTable, LootTableEntry, Enemy, MapInstance, EnemyInstance,
        Battle, BattleLoot, BattleSnapshot,
    )

    Base.metadata.create_all(bind=engine)

    with engine.connect() as conn:
        result = conn.execute(text(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
        ))
        tables = {row[0] for row in result}

    expected = {
        "users", "characters", "maps", "gear_templates", "character_gear",
        "loot_tables", "loot_table_entries", "enemies", "map_instances",
        "enemy_instances", "battles", "battle_loot", "battle_snapshots",
    }
    assert expected <= tables, f"Faltan tablas: {expected - tables}"


def test_character_has_default_stats():
    """Character debe crear con stats por defecto."""
    from app.infrastructure.database.base import Base, engine
    from app.infrastructure.database.models import User, Character
    from app.infrastructure.database.session import SessionLocal

    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        user = User(username="tester", email="t@t.com", hashed_password="xxx")
        db.add(user)
        db.commit()
        db.refresh(user)

        char = Character(user_id=user.id, name="Hero")
        db.add(char)
        db.commit()
        db.refresh(char)

        assert char.hp == 100
        assert char.max_hp == 100
        assert char.atk == 10
        assert char.coins == 0
        assert char.gems == 0
    finally:
        db.close()
