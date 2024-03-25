from pydantic import BaseSettings, BaseModel
from os import getenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class DataBaseSettings(BaseModel):
    database_url: str = getenv("DATABASE_URL")


class JWTSettings(BaseModel):
    private_key: Path = BASE_DIR / "certs" / "private.pem"
    public_key: Path = BASE_DIR / "certs" / "public.pem"
    algorithm: str = "RS256"
    access_token_expires_in: int = 5
    refresh_token_expires_in: int = 30


class Settings(BaseSettings):
    jwt_settings: JWTSettings = JWTSettings()
    database: DataBaseSettings = DataBaseSettings()


settings = Settings()