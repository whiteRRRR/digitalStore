from pydantic import BaseModel, Field


class ProductScheme(BaseModel):
    name: str = Field(max_length=120)
    price: int
    description: str
    is_publush: bool = False

