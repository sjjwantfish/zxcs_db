from redis import Redis
from sqlalchemy.orm import Session

from zxcs_db.config import settings
from zxcs_db.db.redis import get_redis_cli
from zxcs_db.db.session import get_session


def get_db() -> Session:
    db = get_session()
    try:
        yield db
    finally:
        db.close()


def get_redis() -> Redis:
    try:
        cli = get_redis_cli(settings.main.redis)
        yield cli
    finally:
        cli.close()
