from app.repositories.todo_repository import TodoRepository
from schemas.requests.todo_request import TodoRequest, TodoUpdate
from schemas.responses.todo_response import TodoResponse
from app.models.todo_model import TodoModel
from fastapi import HTTPException, status


class TodoService:
    def __init__(self):
        self.todo_repo = TodoRepository()

    def _get_todo_or_raise(self, todo_id: int) -> TodoModel:
        """Helper private method: find todo or raise 404."""
        todo = self.todo_repo.find_by_id(todo_id)
        if not todo:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Todo with id {todo_id} not found",
            )
        return todo

    def create_todo(self, requests: list[TodoRequest]) -> list[TodoResponse]:
        """
        Create a new todo and return its response model.
        Return: TodoResponse
        Raise: 404 if not found
        """
        result: list[TodoResponse] = []
        for request in requests:
            todo = TodoModel(
                todo_id=TodoRepository.next_id(),
                title=request.title,
                description=request.description,
                priority=request.priority,
                done=request.done,
            )
            self.todo_repo.add(todo)
            result.append(TodoResponse.model_validate(todo))

        return result

    def update_todo(self, request: TodoUpdate) -> TodoResponse:
        """
        Update an existing todo (partial update supported).
        Return: TodoResponse
        Raise: 404 if not found
        """
        existed_todo = self._get_todo_or_raise(request.todo_id)

        if request.title is not None:
            existed_todo.title = request.title
        if request.description is not None:
            existed_todo.description = request.description
        if request.priority is not None:
            existed_todo.priority = request.priority
        if request.done is not None:
            existed_todo.done = request.done

        self.todo_repo.update(existed_todo)
        return TodoResponse.model_validate(existed_todo)

    def get_by_id(self, todo_id: int) -> TodoResponse:
        """
        Retrieve a todo by ID.
        Return: TodoResponse
        Raise: 404 if not found
        """
        todo = self._get_todo_or_raise(todo_id)
        return TodoResponse.model_validate(todo)

    def delete_by_id(self, todo_id: int) -> None:
        """
        Delete a todo by ID.
        Return: None
        Raise: 404 if not found
        """
        self._get_todo_or_raise(todo_id)
        self.todo_repo.delete(todo_id)

    def get_all_todos(self) -> list[TodoResponse]:
        """Get all todo"""
        todos = self.todo_repo.get_todos()
        return [TodoResponse.model_validate(t) for t in todos]
