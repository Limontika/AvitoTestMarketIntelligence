import requests

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_add_poll_bad_choice_text():
    response = client.post("/createPoll", json={
        "poll_name": "Тестовое голосование",
        "choice_text": ["Да", "Нет", "Не знаю", "Знаю", "Нет"]
    })
    assert response.status_code == 400
    assert response.json() == {
        "message": str
    }


def test_add_poll():
    response = client.post("/createPoll", json={
        "poll_name": "Тестовое голосование",
        "choice_text": ["Да", "Нет", "Не знаю", "Знаю"]
    })
    assert response.status_code == 200
    assert response.json() == {
        "message": str
    }
