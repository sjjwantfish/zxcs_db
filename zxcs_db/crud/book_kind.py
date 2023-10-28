from zxcs_db.crud.base import BaseCRUD
from zxcs_db.models.book_kind import BookKindModel
from zxcs_db.schemas.book_kind import BookKindCreate, BookKindUpdate


class BookKindCRUD(BaseCRUD[BookKindModel, BookKindCreate, BookKindUpdate]):
    pass


book_kind = BookKindCRUD(BookKindModel)

