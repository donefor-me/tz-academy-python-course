from sqlalchemy.orm import Session

from app.models.todo_model import TodoModel
from sqlalchemy import select

from app.repositories.base import BaseRepository


class TodoRepository(BaseRepository[TodoModel]):
    def __init__(self):
        super().__init__(TodoModel)

    # noinspection PyMethodMayBeStatic
    def get_by_title(self, db: Session, title: str, offset: int, limit: int) -> list[TodoModel]:
        stmt = select(TodoModel).where(TodoModel.title.ilike(f"%{title}%"))
        stmt = stmt.offset(offset).limit(limit)
        return list(db.execute(stmt).scalars().all())

    # noinspection PyMethodMayBeStatic
    def search(self, db: Session, *, done: bool | None, keyword: str | None, offset: int, limit: int) -> list[
        TodoModel]:
        stmt = select(TodoModel)
        if done is not None:
            stmt = stmt.where(TodoModel.done == done)
        if keyword:
            stmt = stmt.where(TodoModel.title.ilike(f"%{keyword}%"))

        stmt = stmt.offset(offset).limit(limit)
        return list(db.execute(stmt).scalars().all())
