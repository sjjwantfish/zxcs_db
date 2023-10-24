from sqlalchemy import create_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker

from zxcs_db.config import MySQLSettings, settings


def get_engine(config: MySQLSettings = settings.main.mysql):
    host = config.host
    port = config.port
    user = config.user
    password = config.password
    dbname = config.db
    encoding = config.encoding

    return create_engine(
        f"mysql+pymysql://{user}:{password}@{host}:{port}/{dbname}",
        pool_pre_ping=True,
        # encoding=encoding,
        pool_recycle=3600,
        pool_use_lifo=True,
    )


default_engine = get_engine(settings.main.mysql)
default_sessionmaker = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=default_engine,
)


def get_scoped_session(config: MySQLSettings = None) -> scoped_session:
    if config is None:
        _sessionmaker = default_sessionmaker
    else:
        _sessionmaker = sessionmaker(
            autocommit=False, autoflush=False, bind=get_engine(config)
        )
    return scoped_session(_sessionmaker)


def get_session(config: MySQLSettings = None) -> Session:
    if config is None:
        _sessionmaker = default_sessionmaker
    else:
        _sessionmaker = sessionmaker(
            autocommit=False, autoflush=False, bind=get_engine(config)
        )
    return _sessionmaker()
