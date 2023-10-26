from sqlalchemy import Column, Integer, String, Text

from zxcs_db.db.base_class import Base


class BookInfoModel(Base):
    __tablename__ = "book_info"

    author = Column(
        "author",
        String(255),
        nullable=False,
        server_default="",
        comment="作者",
    )
    book_name = Column(
        "book_name",
        String(255),
        nullable=False,
        server_default="",
        comment="书名称",
    )
    title = Column(
        "title",
        String(255),
        nullable=False,
        server_default="",
        comment="标题",
    )
    url = Column(
        "url",
        String(255),
        nullable=False,
        server_default="",
        comment="书下载url",
    )
    brief = Column(
        "brief",
        Text(),
        nullable=False,
        # server_default="",
        comment="概要",
    )
    kind_id = Column(
        "kind_id",
        Integer,
        nullable=False,
        server_default=0,
        comment="类ID",
    )
    bad = Column(
        "bad",
        Integer,
        nullable=False,
        server_default=0,
        comment="毒草",
    )
    not_bad = Column(
        "not_bad",
        Integer,
        nullable=False,
        server_default=0,
        comment="枯草",
    )
    normal = Column(
        "normal",
        Integer,
        nullable=False,
        server_default=0,
        comment="干草",
    )
    good = Column(
        "good",
        Integer,
        nullable=False,
        server_default=0,
        comment="粮草",
    )
    very_good = Column(
        "very_good",
        Integer,
        nullable=False,
        server_default=0,
        comment="仙草",
    )
