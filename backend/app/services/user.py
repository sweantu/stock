from typing import Annotated

from fastapi import Depends
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.user import UserCreate, UserResponse
from app.core.database import DbDep
from app.database.repositories.user import UserRepository


class UserService:
    def __init__(self, db: AsyncSession):
        self.user_repository = UserRepository(db)

    async def create(self, user: UserCreate) -> UserResponse:
        return await self.user_repository.create(user)

    async def get(self, user_id: UUID4) -> UserResponse:
        return await self.user_repository.get(user_id)

    async def get_many(self, skip: int = 0, limit: int = 10) -> list[UserResponse]:
        result = await self.user_repository.get_many(skip, limit)
        return list(result)


def get_user_service(db: DbDep) -> UserService:
    return UserService(db=db)


UserServiceDep = Annotated[UserService, Depends(get_user_service)]
