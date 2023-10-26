from sqlalchemy import Column, String

from zxcs_db.db.base_class import Base


class BookKindModel(Base):
    __tablename__ = "book_kind"

    kind_name = Column(
        "kind_name",
        String(255),
        nullable=False,
        server_default="",
        comment="类名称",
    )
