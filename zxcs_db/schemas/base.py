from pydantic import BaseModel, validator


class ValidatedModel(BaseModel):
    @validator("*", pre=True, each_item=True)
    def strip_str_space(cls, v):
        if isinstance(v, str):
            v = v.strip()
        return v


class NoSpaceModel(BaseModel):
    @validator("*", pre=True, each_item=True)
    def no_space(cls, v):
        if isinstance(v, str):
            return v.replace(" ", "")
        return v


class OrmBase(BaseModel):
    class Config:
        orm_mode = True
