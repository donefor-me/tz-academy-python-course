from fastapi import APIRouter
from app.controllers.heath_router import router as health_router
from app.controllers.todo_controller import router as todo_router

api_router = APIRouter()

api_router.include_router(health_router)
api_router.include_router(todo_router)
