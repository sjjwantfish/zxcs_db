from pydantic import Field

from zxcs_db.schemas.base import ValidatedModel


class BookInfoBase(ValidatedModel):
    author: str = Field(..., title="作者")
    book_name: str = Field(..., title="书名称")
    title: str = Field(..., title="标题")
    url: str = Field(..., title="书下载url")
    brief: str = Field(..., title="概要")
    kind_id: int = Field(..., title="类ID")
    bad: int = Field(..., title="毒草")
    not_bad: int = Field(..., title="枯草")
    normal: int = Field(..., title="干草")
    good: int = Field(..., title="粮草")
    very_good: int = Field(..., title="仙草")


class BookInfoCreate(BookInfoBase):
    pass


class BookInfoUpdate(BookInfoBase):
    pass


class BookInfoInDB(BookInfoBase):
    pass
