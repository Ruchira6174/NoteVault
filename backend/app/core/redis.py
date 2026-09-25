import redis
from collections.abc import Generator
from app.core.config import get_settings

settings = get_settings()

# Reusable Redis client instance
redis_client = redis.Redis.from_url(
    settings.REDIS_URL,
    decode_responses=True,
    socket_timeout=5.0
)

def get_redis() -> Generator[redis.Redis, None, None]:
    """
    Redis dependency for FastAPI routes.
    """
    try:
        yield redis_client
    finally:
        # Redis client manages its own connection pool, no need to explicitly close here
        pass

def check_redis_health() -> bool:
    """
    Helper function to check if Redis is accessible.
    """
    try:
        return redis_client.ping()
    except redis.RedisError:
        return False
