from fastapi import APIRouter

from .endpoints import poll, result

api_router = APIRouter()
api_router.include_router(poll.router, prefix="/poll", tags=["poll"])
api_router.include_router(result.router, prefix="/result", tags=["result"])
