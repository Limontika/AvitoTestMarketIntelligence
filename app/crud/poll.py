from bson.objectid import ObjectId

from ..db.base import poll_collection


def add_poll(poll_data: dict) -> str:
    poll = poll_collection.insert_one(poll_data)
    return f"Создано новое голосование с id={poll.inserted_id}"


def update_poll(poll_id: str, choice_id: int) -> str:
    poll = poll_collection.find_one({"_id": ObjectId(poll_id)})
    for index, choice in enumerate(poll['choice_text']):
        if choice_id == index + 1:
            poll['choice_text'][choice] += 1
            break
    updated_poll = poll_collection.update_one({"_id": ObjectId(poll_id)}, {"$set": poll})
    if updated_poll:
        return f"Ваш голос учтён, спасибо что проголосовали"
    return f"Извенити произошла ошибка при учете вашего голоса, повторите попытку или обратитесь к администратору"


def get_result_poll(poll_id: str) -> dict:
    poll = poll_collection.find_one({"_id": ObjectId(poll_id)})
    return poll