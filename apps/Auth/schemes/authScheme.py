from pydantic import BaseModel, Field


class SignUp(BaseModel):
    username: str = Field(max_length=50)
    email: str = Field(max_length=80)
    hashed_password: bytes = Field(min_length=10)


class SignIn(BaseModel):
    username: str = Field(max_length=50)
    password: str = Field(min_length=10)


class UserPayload(BaseModel):
    username: str = Field(max_length=50)
    token: str


class UserInDataBase(BaseModel):
    id: int
    username: str = Field(max_length=50)
    email: str = Field(max_length=80)
    hashed_password: str = Field(min_length=10)


class UserWithToken(BaseModel):
    user_id: int
    refresh_token: str

