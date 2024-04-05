from pydantic import BaseModel, Field


class UserPayload(BaseModel):
    username: str = Field(max_length=50)


class UserInDataBase(BaseModel):
    id: int
    username: str = Field(max_length=50)
    email: str = Field(max_length=80)
    hashed_password: str = Field(min_length=10)


class UserWithToken(BaseModel):
    user_id: int
    refresh_token: str


class UserWithoutPassword(BaseModel):
    username: str = Field(max_length=50)
    email: str = Field(max_length=80)


class UserChangePassword(BaseModel):
    old_password: bytes = Field(min_length=10)
    new_password: bytes = Field(min_length=10)
