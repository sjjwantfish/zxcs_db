from fastapi import APIRouter,Depends, Query

from sqlalchemy.orm import Session
from zxcs_db.schemas.resp import ResponseOK
from zxcs_db import crud
from zxcs_db.api import deps

book_info_api = APIRouter()


@book_info_api.get("/book")
def get_books(
    db: Session = Depends(deps.get_db),
    book_id: int = Query(..., title='book_id')
):
    book = crud.book_info.get(db, book_id)
    return ResponseOK(data=book)
