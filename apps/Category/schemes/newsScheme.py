from pydantic import BaseModel


class NewsScheme(BaseModel):
    name: str
    