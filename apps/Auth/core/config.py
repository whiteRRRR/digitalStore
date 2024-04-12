from pydantic import BaseModel
from pydantic_settings import BaseSettings
from fastapi_mail import ConnectionConfig
from os import getenv
from dotenv import load_dotenv
from pathlib import Path

load_dotenv('apps\\Auth\\.env')


BASE_DIR = Path(__file__).resolve().parent.parent
API_V1_PREFIX = "/api/v1"
SERVER_HOST = getenv("SERVER_HOST")


class DataBaseSettings(BaseModel):
    database_url: str = getenv("DATABASE_URL_AUTH")


class EmailSettings(BaseModel):
    mail_username: str = getenv("EMAIL_USERNAME")
    mail_password: str = getenv("EMAIL_PASSWORD")
    mail_from: str = getenv("EMAIL_FROM")
    mail_port: int = getenv("EMAIL_PORT")
    mail_server: str = getenv("EMAIL_SERVER")
    mail_starttls: bool = getenv("EMAIL_STARTTLS")
    mail_ssl_tls: bool = getenv("EMAIL_SSL_TLS")
    use_credentials: bool = getenv("USE_CREDENTIALS")
    validate_certs: bool = getenv("VALIDATE_CERTS")

    email_conf: ConnectionConfig = ConnectionConfig(
        MAIL_USERNAME=mail_username,
        MAIL_PASSWORD=mail_password,
        MAIL_FROM=mail_from,
        MAIL_PORT=mail_port,
        MAIL_SERVER=mail_server,
        MAIL_STARTTLS=mail_starttls,
        MAIL_SSL_TLS=mail_ssl_tls,
        USE_CREDENTIALS=use_credentials,
        VALIDATE_CERTS=validate_certs
    )


class JWTSettings(BaseModel):
    private_key: Path = BASE_DIR / "certs" / "private.pem"
    public_key: Path = BASE_DIR / "certs" / "public.pem"
    algorithm: str = "RS256"
    access_token_expires_in: int = 5
    refresh_token_expires_in: int = 30


class Settings(BaseSettings):
    jwt_settings: JWTSettings = JWTSettings()
    database: DataBaseSettings = DataBaseSettings()
    email: EmailSettings = EmailSettings()


settings = Settings()
