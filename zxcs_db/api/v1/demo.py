from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from zxcs_db import crud
from zxcs_db.api import deps
from zxcs_db.schemas.resp import ResponseOK

demo_api = APIRouter(
    prefix="/demo",
    tags=["demo"],
)


@demo_api.get("/list")
def get_demo_list(
    # db: Session = Depends(deps.get_db),
    # keywords: str = "",
    # skip: int = 0,
    # limit: int = 100,
):
    # users = crud.user.get_users_by_keywords(
    #     db, keywords=keywords, skip=skip, limit=limit
    # )
    return ResponseOK(data="this is demo list")
