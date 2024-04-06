from fastapi import HTTPException, status


class AuthException(HTTPException):
    def __init__(self, detail: str, headers: dict | None = None) -> None:
        super().__init__(status.HTTP_401_UNAUTHORIZED, detail, headers)


class BadRequestException(HTTPException):
    def __init__(self, detail: str, headers: dict | None = None) -> None:
        super().__init__(status.HTTP_400_BAD_REQUEST, detail, headers)
