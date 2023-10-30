from typing import List

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


@book_info_api.get("/titles")
def get_titles(
    db: Session = Depends(deps.get_db),
    kind_ids: List[int] = Query(..., title="kind_ids"),
):
    result = {}
    for kind_id in kind_ids:
        result[kind_id] = crud.book_info.get_titles_by_kind(db, kind_id)
    
    print(result)
    return ResponseOK(result)

@book_info_api.get("/book_name")
def get_book_name(
    db: Session = Depends(deps.get_db),
    author = Query(..., title="author"),
):
    result = {}
    result[author] = crud.book_info.get_book_name_by_author(db, author)
    
    print(result)
    return ResponseOK(result)
