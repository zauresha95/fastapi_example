from typing import Literal
from pydantic import BaseSettings


class Settings(BaseSettings):
    MODE: Literal['DEV', 'TEST', 'PROD']
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    REDIS_HOST: str
    REDIS_PORT: int

    class Config:
        env_file = ".env"
    # model_config = SettingsConfigDict(env_file=".env")

settings = Settings()