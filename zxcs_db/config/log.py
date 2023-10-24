from loguru import logger

from zxcs_db.config import MainSettings


def init_log(settings: MainSettings):
    logger.add(
        f"{settings.log_dir}/error.log",
        encoding="utf-8",
        compression="zip",
        rotation="1 month",
        retention=10,
        enqueue=True,
        level=settings.log_level.upper(),
    )
