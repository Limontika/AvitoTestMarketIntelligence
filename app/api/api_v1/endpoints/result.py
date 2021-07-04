from fastapi import APIRouter

router = APIRouter()


@router.post("/getResult")
def get_result(poll_id: int):
    pass
