from zxcs_db.crud.base import BaseCRUD
from zxcs_db.models.book_info import BookInfoModel
from zxcs_db.schemas.book_info import BookInfoCreate, BookInfoUpdate


class BookInfoCRUD(BaseCRUD[BookInfoModel, BookInfoCreate, BookInfoUpdate]):
    pass


book_info = BookInfoCRUD(BookInfoModel)
