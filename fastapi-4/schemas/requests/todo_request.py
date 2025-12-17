from pydantic import BaseModel, Field

from core.enums import Measurement, Priority


class TodoRequest(BaseModel):
    title: str = Field(min_length=Measurement.MIN_TITLE)
    description: str | None = None
    priority: Priority = Field(default=Priority.MEDIUM)
    done: bool = False


class TodoUpdate(BaseModel):
    todo_id: int
    title: str | None = Field(default=None, min_length=Measurement.MIN_TITLE)
    description: str | None = None
    priority: Priority | None = None
    done: bool | None = None
