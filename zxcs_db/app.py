import sys
from http.client import HTTPException

from fastapi import FastAPI
from loguru import logger
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR

from zxcs_db import LogLevelEnum, MainSettings, v1_router
from zxcs_db.error import ServerException


def create_app(main_settings: MainSettings) -> FastAPI:
    log_level = main_settings.log_level
    if log_level != LogLevelEnum.debug:
        logger.remove()
        logger.add(sys.stderr, level=log_level.value.upper())

    app = FastAPI(title=main_settings.appname)
    app.add_exception_handler(Exception, base_error_handler)
    app.add_exception_handler(HTTPException, base_error_handler)
    app.add_exception_handler(ServerException, server_error_handler)

    app.include_router(v1_router, prefix="/x51")
    return app


def base_error_handler(request: Request, exc: Exception) -> JSONResponse:
    logger.error(str(exc))
    return JSONResponse(
        {"status": {"msg": str(exc), "code": 500}},
        status_code=HTTP_500_INTERNAL_SERVER_ERROR,
    )


def server_error_handler(_: Request, exc: ServerException) -> JSONResponse:
    logger.error(exc.msg)
    return JSONResponse(
        {"status": {"msg": exc.msg, "code": exc.code}, "data": exc.data},
        status_code=exc.http_code,
    )

# 获取参数
