from pydantic import BaseModel, EmailStr, ConfigDict


class Signin(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str


class Signup(BaseModel):
    email: str
    password: str


class User(BaseModel):
    id: int
    email: str

    model_config = ConfigDict(from_attributes=True)
