from fastapi import APIRouter

from app.crud.poll import update_poll, add_poll
from app.models.base import response_model, error_response_model

router = APIRouter()


@router.post("/createPoll")
def create_poll(poll_name: str,
                choice_text: list):
    if len(choice_text) != len(set(choice_text)):
        error = "Ошибка при создании нового голосования"
        message = f"Несколько одинаковых вариантов ответов"
        raise error_response_model(error=error, code=400, message=message)
    data = {
        "poll_name": poll_name,
        "choice_text": {
            choice_text[i]: 0 for i in range(len(choice_text))
        }
    }
    return response_model(data, add_poll(data))


@router.post("/poll")
def poll(poll_id: str,
         choice_id: int):
    return update_poll(poll_id, choice_id)
