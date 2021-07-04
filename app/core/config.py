import secrets

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    PROJECT_NAME: str = "AVITO Market Intelligence Poll"

    class Config:
        # TODO добавить .env
        pass


settings = Settings()
