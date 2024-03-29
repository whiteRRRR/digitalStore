from pydantic import BaseModel, Field


class SignUp(BaseModel):
    username: str = Field(max_length=50)
    email: str = Field(max_length=80)
    hashed_password: bytes = Field(min_length=10)


class SignIn(BaseModel):
    username: str = Field(max_length=50)
    password: bytes = Field(min_length=10)


class TokenData(BaseModel):
    access_token: str
    token_type: str
