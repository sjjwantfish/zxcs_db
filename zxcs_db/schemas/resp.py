from typing import Any

from fastapi.encoders import jsonable_encoder

# from fastapi
from fastapi.responses import JSONResponse


class ResponseOK(JSONResponse):
    def __init__(
        self,
        data: Any = None,
        msg: Any = "ok",
        status_code: int = 200,
    ) -> None:
        data = jsonable_encoder(data)
        super().__init__(
            {
                "data": data,
                "msg": msg,
                "retcode": 0,
            },
            status_code,
        )


class ResponseNotFound(JSONResponse):
    def __init__(
        self,
        msg: Any = "resource not found...",
    ) -> None:
        super().__init__(
            {
                "msg": msg,
                # TODO(sujiajun): 定义 retcode 规范
                "retcode": 0,
            },
            404,
        )


class ResponseBusinessError(JSONResponse):
    def __init__(
        self,
        msg: Any = "business error...",
    ) -> None:
        super().__init__(
            {
                "msg": msg,
                "retcode": 1101,
            },
            412,
        )


class ParamsError(JSONResponse):
    def __init__(
        self,
        msg: Any = "",
    ) -> None:
        super().__init__(
            {
                "msg": "参数错误！" + msg,
                "retcode": 0,
            },
            400,
        )


class ServerError(JSONResponse):
    def __init__(
        self,
        msg: Any = "",
    ) -> None:
        super().__init__(
            {
                "msg": "服务端错误！" + msg,
                "retcode": 1102,
            },
            500,
        )
