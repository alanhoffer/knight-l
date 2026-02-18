"""Tests de configuración."""

import os

import pytest


def test_settings_load_defaults():
    """Config debe cargar valores por defecto."""
    from app.config import settings

    assert settings.app_name == "IronClash Backend"
    assert settings.app_version == "1.0.0"
    assert settings.algorithm == "HS256"
    assert settings.max_lives == 5


def test_cors_origins_list():
    """CORS origins debe ser lista de strings."""
    from app.config import settings

    origins = settings.cors_origins_list
    assert isinstance(origins, list)
    assert len(origins) >= 2  # Por defecto hay al menos 2 orígenes
    assert all(isinstance(o, str) for o in origins)
