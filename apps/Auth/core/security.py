from datetime import datetime, timedelta

from bcrypt import hashpw, checkpw, gensalt
from jwt import encode, decode
from typing import Any
from core.config import settings


class PasswordSecurity:

    @staticmethod
    async def get_hash_password(password: bytes) -> bytes:
        gen_salt = gensalt()
        hash_password = hashpw(password, gen_salt)
        return hash_password

    @staticmethod
    async def check_password(password, hash_password) -> bool:
        checking_password = checkpw(password, hash_password)
        return checking_password


class JwtSecurity:

    @staticmethod
    async def create_access_token(
            payload: dict,
            private_key: str = settings.jwt_settings.private_key,
            algorithm: str = settings.jwt_settings.algorithm,
            expire_minutes: int = settings.jwt_settings.access_token_expires_in
    ) -> str:
        copy_payload = payload.copy()
        now = datetime.utcnow()
        expire = now + timedelta(minutes=expire_minutes)
        copy_payload.update({"exp": expire, "iat": now})

        encoded_jwt = encode(payload, private_key, algorithm)
        return encoded_jwt

    @staticmethod
    async def create_refresh_token(
            payload: dict,
            private_key: str = settings.jwt_settings.private_key,
            algorithm: str = settings.jwt_settings.algorithm,
            expire_days: int = settings.jwt_settings.refresh_token_expires_in
    ) -> str:
        copy_payload = payload.copy()
        now = datetime.utcnow()
        expire = now + timedelta(days=expire_days)
        copy_payload.update({"exp": expire, "iat": now})

        encoded_jwt = encode(payload, private_key, algorithm)
        return encoded_jwt

    @staticmethod
    async def decode_jwt(
            token: str,
            public_key: str = settings.jwt_settings.public_key,
            algorithm: str = settings.jwt_settings.algorithm,
    ) -> Any:

        decoded_jwt = decode(token, public_key, algorithm)
        return decoded_jwt


class SecurityManager:
    jwt_security: JwtSecurity = JwtSecurity()
    password_security: PasswordSecurity = PasswordSecurity()


security = SecurityManager()
