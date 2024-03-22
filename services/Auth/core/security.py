from bcrypt import hashpw, checkpw, gensalt
from jwt import encode, decode
from typing import Any


class PasswordSecurity:

    @staticmethod
    async def get_hash_password(password) -> bytes:
        hash_password = hashpw(password, gensalt())
        return hash_password

    @staticmethod
    async def check_password(password, hash_password) -> bool:
        checking_password = checkpw(password, hash_password)
        return checking_password


class JwtSecurity:

    @staticmethod
    async def encode_jwt(payload: dict, private_key: str, algorithm: str) -> str:
        encoded_jwt = encode(payload, private_key, algorithm)
        return encoded_jwt

    @staticmethod
    async def decode_jwt(token: str, public_key: str, algorithm:str) -> Any:
        decoded_jwt = decode(token, public_key, algorithm)
        return decoded_jwt


class SecurityManager:
    jwt_security: JwtSecurity = JwtSecurity()
    password_security: PasswordSecurity = PasswordSecurity()


security = SecurityManager()