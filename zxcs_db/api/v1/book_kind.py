from fastapi import APIRouter,Depends, Query

from sqlalchemy.orm import Session
from zxcs_db.schemas.resp import ResponseOK
from zxcs_db import crud
from zxcs_db.api import deps

book_kind_api = APIRouter()


@book_kind_api.get("/kinds")
def get_kinds(
    db: Session = Depends(deps.get_db),
):
    book_kind = crud.book_kind.get_multi(db=db)
    return ResponseOK(data=book_kind)
