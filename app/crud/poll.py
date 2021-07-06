from bson.objectid import ObjectId

from ..db.base import poll_collection
from app.models.base import response_model, error_response_model


def add_poll(poll_data: dict) -> dict:
    poll = poll_collection.insert_one(poll_data)
    return response_model({"id": str(poll.inserted_id)}, f"Создано новое голосование")


def update_poll(poll_id: str, choice_id: int) -> dict:
    poll = poll_collection.find_one({"_id": ObjectId(poll_id)})
    for index, choice in enumerate(poll['choice_text']):
        if choice_id == index + 1:
            poll['choice_text'][choice] += 1
            break
    else:
        return error_response_model({"poll_id": poll_id, "choice_id": choice_id}, 404,
                              f"Варианта ответа с таким id: {choice_id} не существует")
    updated_poll = poll_collection.update_one({"_id": ObjectId(poll_id)}, {"$set": poll})
    if updated_poll:
        return response_model("", f"Ваш голос учтён, спасибо что проголосовали")
    return error_response_model("Ошибка при учете вашего голоса", 404,
                                f"Повторите попытку или обратитесь к администратору")


def get_result_poll(poll_id: str) -> dict:
    poll = poll_collection.find_one({"_id": ObjectId(poll_id)})
    data = {
        "poll_name": poll['poll_name'],
        "choice_text": poll['choice_text']
    }
    if poll:
        return response_model(data, f"Результаты по голосованию {poll['poll_name']}")
    return error_response_model("Не существует указанного голосования", 404,
                                "Проверьте данные или обратитесь к администратору")
