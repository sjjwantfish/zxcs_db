from fastapi import APIRouter

from zxcs_db.api.v1.book_info import book_info_api
from zxcs_db.api.v1.book_kind import book_kind_api
from zxcs_db.api.v1.demo import demo_api


v1_router = APIRouter(prefix="/api/v1")
v1_router.include_router(demo_api)
v1_router.include_router(book_info_api)
v1_router.include_router(book_kind_api)
