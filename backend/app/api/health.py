"""Health check endpoint."""

import logging

from fastapi import APIRouter
from sqlalchemy import text

from app.config import settings
from app.infrastructure.database.base import engine

router = APIRouter(tags=["health"])
logger = logging.getLogger(__name__)


def _check_redis() -> str:
    """Check Redis connectivity. Returns 'ok', 'unavailable', or 'skipped'."""
    try:
        from app.infrastructure.cache.redis_client import redis_client
        redis_client.ping()
        return "ok"
    except ImportError:
        return "skipped"
    except Exception as e:
        logger.warning("Health check: redis unavailable", extra={"error": str(e)})
        return "unavailable"


@router.get("/health")
async def health_check():
    """
    Health check: verifica conectividad con DB y Redis.
    Returns 200 si DB ok. Redis opcional (no falla si no está).
    """
    status = "healthy"
    checks = {}

    # Database
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        checks["database"] = "ok"
    except Exception as e:
        logger.error("Health check: database error", extra={"error": str(e)})
        checks["database"] = "error"
        status = "unhealthy"

    # Redis (opcional)
    checks["redis"] = _check_redis()

    return {
        "status": status,
        "app": settings.app_name,
        "version": settings.app_version,
        "environment": settings.environment,
        "checks": checks,
    }
