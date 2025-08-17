from fastapi import APIRouter
from sqlalchemy.future import select

from app.core.database import DbDep
from app.database.models.user import User

router = APIRouter()


@router.get("/")
async def get_many(db: DbDep):
    result = await db.execute(select(User))
    return result.scalars().all()
