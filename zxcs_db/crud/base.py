from datetime import datetime
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from zxcs_db.db.base_class import Base, BaseStatus
from zxcs_db.error import NotFoundError

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseCRUD(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to CRUD.

        params
            model: A SQLAlchemy model class
            schema: A Pydantic model (schema) class
        """
        self.model = model

    def get(self, db: Session, _id: Any) -> Optional[ModelType]:
        if hasattr(self.model, "status"):
            return (
                db.query(self.model)
                .filter(
                    self.model.id == _id,
                    self.model.status != BaseStatus.deleted,
                )
                .first()
            )
        return db.query(self.model).filter(self.model.id == _id).first()

    def get_last(self, db: Session) -> Optional[ModelType]:
        return db.query(self.model).order_by(self.model.id.desc()).first()

    # @catch_db_error
    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(
        self,
        db: Session,
        obj_in: Union[CreateSchemaType, dict[str, Any], ModelType],
        auto_commit: bool = True,
    ) -> ModelType:
        if isinstance(obj_in, dict):
            obj_in_data = obj_in
        else:
            obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(
            **obj_in_data,
            create_time=datetime.now(),
            update_time=datetime.now(),
        )
        add_model(db, db_obj)
        if auto_commit is True:
            commit(db)
        return db_obj

    @classmethod
    def update(
        cls,
        db: Session,
        db_obj: ModelType,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]] = None,
        auto_commit: bool = True,
        **kwargs
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if obj_in is not None:
            if isinstance(obj_in, dict):
                update_data = obj_in
            else:
                update_data = obj_in.dict(exclude_unset=True)
            for field in obj_data:
                if field in update_data:
                    setattr(db_obj, field, update_data[field])
        setattr(db_obj, "update_time", datetime.now())
        merge_model(db, db_obj)
        if auto_commit is True:
            commit(db)
        return db_obj

    def remove(self, db: Session, *, _id: int, auto_commit=True) -> ModelType:
        """remove from db"""
        obj = db.query(self.model).get(_id)
        delete_model(db, obj)
        if auto_commit is True:
            commit(db)
        return obj

    def delete(self, db: Session, *, _id: int, auto_commit=True) -> int:
        """mark db_obj as deleted"""
        obj = self.get(db, _id)
        if not obj:
            raise NotFoundError(_id)
        if hasattr(obj, "status"):
            obj.status = BaseStatus.deleted
            merge_model(db, obj)
        else:
            delete_model(db, obj)
        if auto_commit is True:
            commit(db)
        return _id


def merge_model(db: Session, model):
    try:
        db.merge(model)
        db.flush()
    except Exception as e:
        db.rollback()
        raise e
    return model


def add_model(db: Session, model):
    try:
        db.add(model)
        db.flush()
    except Exception as e:
        db.rollback()
        raise e
    return model


def commit(db: Session):
    try:
        db.commit()
    except Exception as e:
        db.rollback()
        raise e


def commit_models(db: Session, models):
    try:
        db.add_all(models)
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    return models


def delete_model(db: Session, model):
    try:
        db.delete(model)
        db.flush()
    except Exception as e:
        db.rollback()
        raise e
    return model
