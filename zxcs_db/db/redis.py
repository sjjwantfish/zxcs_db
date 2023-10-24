import redis

from zxcs_db.config.settings import RedisSettings, settings


def get_redis_cli(settings: RedisSettings = settings.main.redis) -> redis.Redis:
    return redis.Redis(
        connection_pool=redis.ConnectionPool(
            host=settings.host,
            port=settings.port,
            db=settings.db,
            decode_responses=True,
        )
    )


def init_redis(settings: RedisSettings):
    redis_client = get_redis_cli(settings)
    try:
        redis_client.ping()
    except redis.exceptions.ConnectionError:
        raise RuntimeError("Redis server is not running")

    return redis_client


redis_proxy = init_redis(settings.main.redis)
