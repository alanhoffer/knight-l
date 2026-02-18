"""Redis client for caching and sessions."""

import redis

from app.config import settings

redis_client = redis.from_url(
    settings.redis_url,
    decode_responses=True,
)


def get_redis():
    """Return Redis client."""
    return redis_client
