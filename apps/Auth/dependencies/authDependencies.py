from fastapi import Request
from core.security import security
from core.exceptions import AuthException
from jwt.exceptions import InvalidSignatureError


async def check_authenticate(request: Request) -> str:
    cookie_data = request.cookies.get("auth")
    if cookie_data is None:
        raise AuthException("No cookie found")
    try:
        token_info = await security.jwt_security.decode_jwt(cookie_data)
        print(token_info)
    except InvalidSignatureError:
        raise AuthException("Token invalid")

    return token_info["username"]








