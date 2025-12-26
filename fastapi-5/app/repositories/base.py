from typing import Any, Generic, Type, TypeVar, List
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.base import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get_by_id(self, db: Session, entity_id: Any) -> ModelType | None:
        stmt = select(self.model).where(self.model.id == entity_id)  # type: ignore[attr-defined]
        return db.execute(stmt).scalars().first()

    def get_all(self, db: Session, *, offset: int = 0, limit: int = 100) -> List[ModelType]:
        stmt = select(self.model).offset(offset).limit(limit)
        return list(db.execute(stmt).scalars().all())

    # noinspection PyMethodMayBeStatic
    def create(self, db: Session, obj: ModelType) -> ModelType:
        db.add(obj)
        db.flush()
        db.refresh(obj)
        return obj

    # noinspection PyMethodMayBeStatic
    def update(self, db: Session, obj: ModelType, data: dict[str, Any]) -> ModelType:
        for field, value in data.items():
            setattr(obj, field, value)
        db.flush()
        db.refresh(obj)
        return obj

    # noinspection PyMethodMayBeStatic
    def delete(self, db: Session, obj: ModelType) -> None:
        db.delete(obj)
        db.flush()

    # noinspection PyMethodMayBeStatic
    def bulk_create(self, db: Session, objs: List[ModelType]) -> List[ModelType]:
        if not objs:
            return []
        db.add_all(objs)
        db.flush()
        for obj in objs:
            db.refresh(obj)
        return objs
