from pydantic import BaseModel
from pydantic_settings import BaseSettings
from os import getenv, path
from dotenv import load_dotenv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
API_V1_PREFIX = "/api/v1"

dotenv_path = path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path)


class DataBaseSettings(BaseModel):
    database_url: str = getenv("DATABASE_URL_CATEGORY")


class Settings(BaseSettings):
    database: DataBaseSettings = DataBaseSettings()


settings = Settings()
