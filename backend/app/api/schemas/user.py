from pydantic import UUID4, BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr


class UserResponse(BaseModel):
    id: UUID4
    name: str
    email: EmailStr

    class Config:
        from_attributes = True
