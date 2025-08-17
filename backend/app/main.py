from fastapi import FastAPI

from app.api.routes.user import router as user_router
from app.core.database import health_check as health_check_db

app = FastAPI(root_path="/api")


@app.get("/")
def read_root():
    return {"message": "Hello FastAPI 🚀"}

@app.get("/health")
async def health_check():
    return await health_check_db()


app.include_router(user_router, prefix="/users", tags=["users"])