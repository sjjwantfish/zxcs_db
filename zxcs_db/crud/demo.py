from zxcs_db.crud.base import BaseCRUD
from zxcs_db.models.demo import DemoModel
from zxcs_db.schemas.demo import (
    DemoCreate,
    DemoUpdate,
)


class DemoCRUD(BaseCRUD[DemoModel, DemoCreate, DemoUpdate]):
    pass

demo = DemoCRUD(DemoModel)
