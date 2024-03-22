from pydantic import BaseModel, Field


class User(BaseModel):
    username: str
    email: str = Field(max_length=80)


class RegisterUser(User):
    password: str = Field(min_length=8)


class LoginUser(User):
    pass

