
from pydantic import Field
from pydantic import BaseModel, validator

from zxcs_db.schemas.base import ValidatedModel


class DemoBase(BaseModel):
    name: str = Field(title="名")


class DemoCreate(DemoBase):
    pass


class DemoUpdate(DemoCreate):
    pass

