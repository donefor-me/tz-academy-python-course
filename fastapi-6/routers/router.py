from fastapi import APIRouter
from app.controllers.todo_controller import router as todo_router

api_router = APIRouter()

api_router.include_router(todo_router)
