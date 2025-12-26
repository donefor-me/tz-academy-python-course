from fastapi import APIRouter, status, Depends, Query
from typing import List
from sqlalchemy.orm import Session
from fastapi import Response

from app.services.todo_service import TodoService
from schemas.requests.todo_request import TodoRequest, TodoUpdate
from schemas.responses.todo_response import TodoResponse
from dependencies.db import get_db

router = APIRouter(prefix="/todos", tags=["Todos"])


def get_todo_service(db: Session = Depends(get_db)) -> TodoService:
    return TodoService(db)


@router.post(
    "/",
    response_model=TodoResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_todos(
        request: TodoRequest,
        response: Response,
        service: TodoService = Depends(get_todo_service)
) -> TodoResponse:
    """Create new todo items."""
    todo = service.create_todo(request)
    response.headers["Location"] = f"/todos/{todo.id}"
    return todo


@router.get("/{todo_id}", response_model=TodoResponse,
            status_code=status.HTTP_200_OK)
async def get_todo_by_id(
        todo_id: int,
        service: TodoService = Depends(get_todo_service)
) -> TodoResponse:
    """Retrieve a todo by its ID."""
    return service.get_by_id(todo_id)


@router.get("/", response_model=List[TodoResponse],
            status_code=status.HTTP_200_OK)
async def get_all_todos(
        offset: int = Query(0, ge=0),
        limit: int = Query(10, ge=1, le=100),
        service: TodoService = Depends(get_todo_service)
) -> List[TodoResponse]:
    """Retrieve all todos with pagination."""
    return service.get_all_todos(offset=offset, limit=limit)


@router.put("/{todo_id}", response_model=TodoResponse, status_code=status.HTTP_200_OK)
async def update_todo(
        todo_id: int,
        todo_update: TodoUpdate,
        service: TodoService = Depends(get_todo_service)
) -> TodoResponse:
    """Update an existing todo."""
    todo_update.todo_id = todo_id
    todo = service.update_todo(todo_update)
    return todo


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(
        todo_id: int,
        service: TodoService = Depends(get_todo_service)
) -> None:
    """Delete a todo by ID."""
    service.delete_by_id(todo_id)
    return None


@router.get("/find-by-title/{title}", response_model=List[TodoResponse], status_code=status.HTTP_200_OK)
async def find_by_title(
        title: str,
        offset: int = Query(0, ge=0),
        limit: int = Query(10, ge=1, le=100),
        service: TodoService = Depends(get_todo_service)
) -> List[TodoResponse]:
    """Retrieve all todos with pagination."""
    return service.find_by_title(title=title, offset=offset, limit=limit)
