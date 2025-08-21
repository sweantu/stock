from pydantic import BaseModel, EmailStr

from app.api.schemas.user import UserResponse


class Login(BaseModel):
    email: EmailStr
    password: str


class AuthResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse
