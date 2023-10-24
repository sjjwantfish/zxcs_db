import os
from loguru import logger

from pydantic_settings import BaseSettings

from zxcs_db.config.options import LogLevelEnum, ServerModeEnum
from zxcs_db.config.yamlconfig import get_config


class MySQLSettings(BaseSettings):
    host: str
    port: int = 3306
    user: str
    password: str
    db: str
    encoding: str = "utf-8"


class RedisSettings(BaseSettings):
    host: str = "127.0.0.1"
    port: int = 6379
    db: int = 0
    decode_responses: bool = True


class MainSettings(BaseSettings):
    appname: str
    server_mode: ServerModeEnum = ServerModeEnum.local
    log_dir: str = "logs/"
    log_level: LogLevelEnum = LogLevelEnum.debug
    listen: str = "0.0.0.0"
    port: int = 8080
    workers: int = os.cpu_count()
    mysql: MySQLSettings
    redis: RedisSettings = RedisSettings()


class AppSettings(BaseSettings):
    main: MainSettings


def init_settings() -> AppSettings:
    app_settings = AppSettings(**get_config())
    return app_settings


settings = init_settings()
logger.info(settings)
