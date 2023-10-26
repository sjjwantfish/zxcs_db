from sqlalchemy import VARCHAR, Column, Integer, Text

from zxcs_db.db.base_class import Base


class BookInfoModel(Base):
    __tablename__ = "book_info"

    author = Column(VARCHAR(255), nullable=False, server_default="", comment="作者")
    book_name = Column(VARCHAR(255), nullable=False, server_default="", comment="书名称")
    title = Column(
        VARCHAR(255),
        nullable=False,
        server_default="",
        comment="标题",
    )
    url = Column(
        VARCHAR(255),
        nullable=False,
        server_default="",
        comment="书下载url",
    )
    brief = Column(
        Text(),
        nullable=False,
        comment="概要",
    )
    kind_id = Column(Integer, nullable=False, comment="类ID")
    bad = Column(Integer, nullable=False, comment="毒草")
    not_bad = Column(Integer, nullable=False, comment="枯草")
    normal = Column(Integer, nullable=False, comment="干草")
    good = Column(Integer, nullable=False, comment="粮草")
    very_good = Column(Integer, nullable=False, comment="仙草")
