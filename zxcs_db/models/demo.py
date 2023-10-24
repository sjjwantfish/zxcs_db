from enum import Enum

from sqlalchemy import Column, DateTime, DefaultClause
from sqlalchemy.dialects.mysql import INTEGER, JSON, TINYINT, VARCHAR
from sqlalchemy.sql.elements import TextClause

from zxcs_db.db import Base
from zxcs_db.db.base_class import BaseStatus



class DemoModel(Base):
    __tablename__ = "demo"
    name = Column(
        "name",
        VARCHAR(20),
        nullable=False,
        server_default=DefaultClause(TextClause("2022-09")),
        comment="demo name",
    )
