from fastapi import APIRouter, status
from typing import List, Any, Coroutine

from scripts.init_todo import init_todo
from services.todo_service import TodoService
from schemas.requests.todo_request import TodoRequest, TodoUpdate
from schemas.responses.todo_response import TodoResponse

router = APIRouter(prefix="/todos", tags=["Todos"])

todo_service = TodoService()


@router.get("/init-data", status_code=status.HTTP_201_CREATED)
async def init_data() -> str:
    init_todo()
    return "OK"


@router.post(
    "/", response_model=list[TodoResponse], status_code=status.HTTP_201_CREATED
)
async def create_todo(request: list[TodoRequest]) -> list[TodoResponse]:
    """
    Create a new todo item.
    """
    todo = todo_service.create_todo(request)
    return todo


@router.get("/{todo_id}", response_model=TodoResponse)
async def get_todo(todo_id: int) -> TodoResponse:
    """
    Retrieve a todo by its ID.
    """
    todo = todo_service.get_by_id(todo_id)
    return todo


@router.get("/", response_model=List[TodoResponse], status_code=status.HTTP_200_OK)
async def get_all_todos() -> list[TodoResponse]:
    """
    Retrieve all todos.
    """
    todos = todo_service.get_all_todos()
    return todos


@router.put(
    "/{todo_id}", response_model=TodoResponse, status_code=status.HTTP_200_OK
)
async def update_todo(todo_id: int, todo_update: TodoUpdate) -> TodoResponse:
    """
    Update a todo
    """
    todo_update.todo_id = todo_id
    todo = todo_service.update_todo(todo_update)
    return todo


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: int) -> None:
    """
    Delete a todo by ID.
    """
    todo_service.delete_by_id(todo_id)
    return None
