from pydantic import Field

from zxcs_db.schemas.base import ValidatedModel


class BookKindBase(ValidatedModel):
    kind_name: str = Field(..., title="类名称")


class BookKindCreate(BookKindBase):
    pass


class BookKindUpdate(BookKindBase):
    pass


class BookKindInDB(BookKindBase):
    pass
