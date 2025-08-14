from fastapi import APIRouter

from app.core.database import DbDep
from app.database.models.user import User

router = APIRouter()


@router.get("/")
async def get_many(db: DbDep):
    return db.query(User).all()
