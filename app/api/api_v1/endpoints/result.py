from fastapi import APIRouter

from app.crud.poll import get_result_poll

router = APIRouter()


@router.post("/getResult")
def get_result(poll_id: str):
    return get_result_poll(poll_id)
