class ServerException(Exception):
    def __init__(self, msg, code=500, data=None, http_code=500):
        self.msg = msg
        self.code = code
        self.data = data
        self.http_code = http_code


class NotLoginException(ServerException):
    def __init__(self, msg="not login", code=401, data=None, http_code=401):
        super().__init__(msg, code, data, http_code)


class PermissionException(ServerException):
    def __init__(self, msg="permission denied", code=403, data=None, http_code=403):
        super().__init__(msg, code, data, http_code)


class NodePermissionError(ServerException):
    def __init__(self, msg, data=None):
        super(NodePermissionError, self).__init__(msg, 1001, data, 403)


class ReleaseStageFinishedError(ServerException):
    def __init__(
        self, msg="release stage finished", code=400, data=None, http_code=400
    ):
        super().__init__(msg, code, data, http_code)


class ReleaseStageFixedVersionError(ServerException):
    def __init__(
        self,
        msg="release stage fixed version error",
        code=400,
        data=None,
        http_code=400,
    ):
        super().__init__(msg, code, data, http_code)


class ReleaseNodeSkipError(ServerException):
    def __init__(
        self,
        msg="node can't not skip",
        code=400,
        data=None,
        http_code=400,
    ):
        super().__init__(msg, code, data, http_code)


class ReleaseStageDependencyError(ServerException):
    def __init__(
        self, msg="release stage dependency error", code=400, data=None, http_code=400
    ):
        super().__init__(msg, code, data, http_code)


class WeComTokenError(ServerException):
    def __init__(self, msg="wecom token error", code=400, data=None, http_code=400):
        super().__init__(msg, code, data, http_code)


class ReleaseStageFixedVersionNoChangeError(ServerException):
    def __init__(
        self,
        msg="release stage fixed version no change",
        code=400,
        data=None,
        http_code=400,
    ):
        super().__init__(msg, code, data, http_code)


class NoClientPackError(ServerException):
    def __init__(self, msg="no client pack", code=400, data=None, http_code=400):
        super().__init__(msg, code, data, http_code)


class NotFoundError(ServerException):
    def __init__(self, _id, code=404, data=None, http_code=404):
        super().__init__(
            msg=f"resource {_id} not found...",
            code=code,
            data=data,
            http_code=http_code,
        )


class UploadPathError(ServerException):
    def __init__(self, msg="找不到上传目录", code=400, data=None, http_code=400):
        super().__init__(msg, code, data, http_code)


class P4PrintError(ServerException):
    def __init__(self, msg="print error", code=400, data=None, http_code=400) -> None:
        super().__init__(msg, code, data, http_code)


class FeatureExcelParseError(ServerException):
    def __init__(self, msg="表格解析错误", code=500, data=None, http_code=500):
        super().__init__(msg, code, data, http_code)


class RepeatExecError(ServerException):
    def __init__(self, msg="不可重复执行", code=1002, data=None, http_code=500):
        super().__init__(msg, code, data, http_code)


class ParamsError(ServerException):
    def __init__(self, msg="参数错误", extra_msg="", code=1003, data=None, http_code=400):
        if extra_msg:
            msg = f"{msg},{extra_msg}"
        super().__init__(msg, code, data, http_code)
