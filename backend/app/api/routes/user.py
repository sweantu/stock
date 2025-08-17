from fastapi import APIRouter
from pydantic import UUID4

from app.api.schemas.user import UserCreate, UserResponse
from app.services.user import UserServiceDep

router = APIRouter()

@router.post("/", response_model=UserResponse)
async def create(user: UserCreate, user_service: UserServiceDep):
    return await user_service.create(user)

@router.get("/{user_id}", response_model=UserResponse)
async def get(user_id: UUID4, user_service: UserServiceDep):
    return await user_service.get(user_id)

@router.get("/", response_model=list[UserResponse])
async def get_many(user_service: UserServiceDep, skip: int = 0, limit: int = 10):
    return await user_service.get_many(skip, limit)