from datetime import datetime

from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.declarative import as_declarative


@as_declarative()
class Base:
    id = Column(Integer, primary_key=True)
    create_time = Column(DateTime, default=datetime.now(), comment="创建时间")
    update_time = Column(DateTime, default=datetime.now(), comment="更新时间")

    def dict(self):
        d = {k: v for k, v in vars(self).items() if not k.startswith("_")}
        return d


class BaseStatus:
    """
    状态
    """

    deleted = -1
