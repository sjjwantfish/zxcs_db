from fastapi import APIRouter
from zxcs_db.api.v1.demo import demo_api

v1_router = APIRouter(prefix="/api/v1")
v1_router.include_router(demo_api)
