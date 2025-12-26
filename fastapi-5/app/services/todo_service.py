from sqlalchemy.orm import Session

from app.repositories.todo_repository import TodoRepository
from exceptions.business_exception import TodoNotFoundException
from schemas.requests.todo_request import TodoRequest, TodoUpdate
from schemas.responses.todo_response import TodoResponse
from app.models.todo_model import TodoModel


class TodoService:
    def __init__(self, db_session: Session):
        self.db_session = db_session
        self.todo_repository = TodoRepository()

    def create_todo(self, requests: TodoRequest) -> TodoResponse:
        created_objs = self.todo_repository.create(self.db_session, TodoModel(
            title=requests.title,
            description=requests.description,
            priority=requests.priority,
            done=requests.done,
        ))
        return TodoResponse.model_validate(created_objs)

    def update_todo(self, request: TodoUpdate) -> TodoResponse:
        existed_todo = self._get_todo_or_raise(request.todo_id)
        # Remove None
        normalized_data = request.model_dump(exclude_unset=True)
        updated_todo = self.todo_repository.update(self.db_session, existed_todo, normalized_data)
        return TodoResponse.model_validate(updated_todo)

    def get_by_id(self, todo_id: int) -> TodoResponse:
        todo = self._get_todo_or_raise(todo_id)
        return TodoResponse.model_validate(todo)

    def delete_by_id(self, todo_id: int) -> None:
        existed_todo = self._get_todo_or_raise(todo_id)
        self.todo_repository.delete(self.db_session, existed_todo)

    def get_all_todos(self, offset: int, limit: int) -> list[TodoResponse]:
        todos = self.todo_repository.get_all(self.db_session, offset=offset, limit=limit)
        return [TodoResponse.model_validate(t) for t in todos]

    def find_by_title(self, title: str, offset: int, limit: int) -> list[TodoResponse]:
        founded = self.todo_repository.get_by_title(self.db_session, title, offset, limit)
        return [TodoResponse.model_validate(t) for t in founded]

    def _get_todo_or_raise(self, todo_id: int) -> TodoModel:
        """Helper private method: find todo or raise 404."""
        todo = self.todo_repository.get_by_id(self.db_session, todo_id)
        if not todo:
            raise TodoNotFoundException(todo_id)
        return todo
