from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from zxcs_db import crud
from zxcs_db.api import deps
from zxcs_db.error import NotFoundError
from zxcs_db.schemas.resp import ResponseOK

book_info_api = APIRouter()


@book_info_api.get("/book")
def get_books(
    db: Session = Depends(deps.get_db),
    book_id: int = Query(..., title="book_id"),
):
    book = crud.book_info.get(db, book_id)
    if not book:
        return NotFoundError(_id=book_id)
    return ResponseOK(data=book)
