from pydantic import BaseModel, EmailStr


class Signin(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str


class Signup(BaseModel):
    email: str
    password: str
