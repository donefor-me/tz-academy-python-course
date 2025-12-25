from fastapi import APIRouter
from sqlalchemy import text
from cores.database import SessionLocal

router = APIRouter()


@router.get("/health/db")
def health_db():
    db = SessionLocal()
    try:
        db.execute(text("SELECT 1"))
        return {"status": "ok"}
    finally:
        db.close()
