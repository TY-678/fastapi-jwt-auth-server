from pydantic import BaseModel


class Token(BaseModel):
    access_token: str


class LoginRequest(BaseModel):
    username: str
    password: str
