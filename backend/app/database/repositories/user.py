import uuid
from datetime import UTC, datetime

from fastapi import HTTPException
from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.api.schemas.user import UserCreate, UserUpdate
from app.core.paging import Paging
from app.core.password import hash_password
from app.database.models.user import Role, User, UserFilter


class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, user_create: UserCreate) -> User:
        user = User(
            name=user_create.name,
            email=user_create.email,
            password=hash_password(user_create.password),
            role=user_create.role,
        )
        self.db.add(user)
        await self.db.flush()  # Ensure the user is created and has an ID
        await self.db.refresh(user)  # Refresh to get the latest state
        return user

    async def get(self, user_id: uuid.UUID) -> User:
        result = await self.db.execute(select(User).where(User.id == user_id))
        user = result.scalars().first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    async def get_by_email(self, email: str) -> User | None:
        result = await self.db.execute(select(User).where(User.email == email))
        return result.scalars().first()

    async def get_many(self, paging: Paging, filter: UserFilter) -> list[User]:
        stmt = select(User)
        stmt = filter.apply(stmt)
        stmt = paging.apply(stmt, User.created_at)
        result = await self.db.execute(stmt)
        return list(result.scalars().all())

    async def count(self, filter: UserFilter) -> int:
        stmt = select(func.count()).select_from(User)
        stmt = filter.apply(stmt)
        count = await self.db.scalar(stmt)
        return count or 0

    async def update(self, user_id: uuid.UUID, user_update: UserUpdate) -> User:
        user = await self.get(user_id)
        user.name = user_update.name
        await self.db.flush()
        await self.db.refresh(user)
        return user

    async def update_password(self, user_id: uuid.UUID, password: str) -> User:
        user = await self.get(user_id)
        user.password = hash_password(password)
        await self.db.flush()
        await self.db.refresh(user)
        return user

    async def update_role(self, user_id: uuid.UUID, role: Role) -> User:
        user = await self.get(user_id)
        user.role = role
        await self.db.flush()
        await self.db.refresh(user)
        return user

    async def deactivate(self, user_id: uuid.UUID) -> User:
        user = await self.get(user_id)
        if user.deleted_at is not None:
            raise HTTPException(status_code=400, detail="User already deactivated")
        user.deleted_at = datetime.now(UTC)
        await self.db.flush()
        await self.db.refresh(user)
        return user

    async def reactivate(self, user_id: uuid.UUID) -> User:
        user = await self.get(user_id)
        if user.deleted_at is None:
            raise HTTPException(status_code=400, detail="User already reactivated")
        user.deleted_at = None
        await self.db.flush()
        await self.db.refresh(user)
        return user