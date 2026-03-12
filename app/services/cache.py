import redis
import os
from dotenv import load_dotenv

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
redis_client = redis.from_url(REDIS_URL)

def cache_set(key: str, value: str, ttl: int = 3600):
    redis_client.setex(key, ttl, value)

def cache_get(key: str):
    return redis_client.get(key)
