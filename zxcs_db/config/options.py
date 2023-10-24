from enum import Enum


class LogLevelEnum(str, Enum):
    debug = "debug"
    info = "info"
    warning = "warning"
    error = "error"


class ServerModeEnum(str, Enum):
    local = "LOCAL"
    dev = "DEVELOPMENT"
    test = "TESTING"
    prod = "PRODUCTION"
