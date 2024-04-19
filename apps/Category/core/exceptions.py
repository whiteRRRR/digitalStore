from typing import Any, Dict
from typing_extensions import Annotated, Doc
from fastapi import HTTPException, status

class BadRequestException(HTTPException):
    def __init__(self, detail: str, headers: Dict[str, str] | None = None) -> None:
        super().__init__(status.HTTP_400_BAD_REQUEST, detail, headers)
