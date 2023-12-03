from pydantic import BaseModel, EmailStr, ConfigDict


class Signin(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str


class Signup(BaseModel):
    email: str
    password: str


class BaseResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)


class User(BaseResponse):
    id: int
    email: str

