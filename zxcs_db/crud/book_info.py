from sqlalchemy.orm import Session

from zxcs_db.crud.base import BaseCRUD
from zxcs_db.models.book_info import BookInfoModel
from zxcs_db.schemas.book_info import BookInfoCreate, BookInfoUpdate


class BookInfoCRUD(BaseCRUD[BookInfoModel, BookInfoCreate, BookInfoUpdate]):
    def get_titles_by_kind(self, db: Session, kind_id: int, limit: int = 8):
        """通过 kind_id 获取 book_info.title"""
        return (
            db.query(self.model)  # select `book_info`
            .filter(self.model.kind_id == kind_id)  # where
            .with_entities(
                self.model.title
            )  # select `book_info`.`title` from `book_info`
            .order_by(self.model.create_time)
            .limit(limit)
            .all()
        )


book_info = BookInfoCRUD(BookInfoModel)
