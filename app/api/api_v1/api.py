from fastapi import APIRouter

from .endpoints import poll, result

api_router = APIRouter()
api_router.include_router(poll.router, tags=["poll"])
api_router.include_router(result.router, tags=["result"])
