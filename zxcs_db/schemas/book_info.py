from pydantic import Field

from zxcs_db.schemas.base import ValidatedModel


class BookInfoBase(ValidatedModel):
    author: str = Field(..., title="作者")
    book_name: str = Field(..., title="书名称")
    title: str = Field(..., title="标题")
    url: str = Field(..., title="书下载url")
    brief: str = Field(..., title="概要")
    # TODO: 补全


class BookInfoCreate(BookInfoBase):
    pass


class BookInfoUpdate(BookInfoBase):
    pass


class BookInfoInDB(BookInfoBase):
    pass
