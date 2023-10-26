import sys

import uvicorn
from loguru import logger

from zxcs_db.app import create_app
from zxcs_db.config import settings
from zxcs_db.config.log import init_log
from zxcs_db.config.options import ServerModeEnum
from zxcs_db.db.init_db import init_db
from zxcs_db.db.redis import init_redis
from zxcs_db.schemas.resp import ResponseOK

# test git
# init settings
main_settings = settings.main
mysql_settings = settings.main.mysql
redis_settings = settings.main.redis
# init log
init_log(main_settings)
# init db
init_db(mysql_settings)
# init redis
init_redis(redis_settings)

app = create_app(main_settings)


@app.get("/healthz", tags=["start"])
def healthz():
    return ResponseOK()


def start_app():
    logger.info(f"======= starting {main_settings.appname} =======")
    logger.info(f"docs url: http://127.0.0.1:{main_settings.port}/docs")
    uvicorn.run(
        app="main:app",
        host=main_settings.listen,
        port=main_settings.port,
        reload=main_settings.server_mode != ServerModeEnum.prod,
        workers=main_settings.workers,
    )


if __name__ == "__main__":
    start_app()
    sys.exit(-1)
