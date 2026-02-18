"""Shared utilities for models."""

from datetime import datetime, timezone


def _utc_now():
    return datetime.now(timezone.utc)
