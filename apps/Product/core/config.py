from pydantic import BaseModel
from pydantic_settings import BaseSettings
from pathlib import Path
from os import path, getenv
from dotenv import load_dotenv


BASE_DIR = Path(__file__).parent.parent
API_V1 = "/api/v1"
ENV_PATH = path.join(BASE_DIR, ".env")

load_dotenv(ENV_PATH)


class DataBase(BaseModel):
    database_url: str = getenv("DATABASE_URL_PRODUCT") # type: ignore


class Settings(BaseSettings):
    database: DataBase = DataBase()


settings = Settings()