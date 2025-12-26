from pydantic import BaseModel, Field

from cores.enums import Measurement, Priority


class TodoRequest(BaseModel):
    title: str = Field(min_length=Measurement.MIN_TITLE_LENGTH)
    description: str | None = None
    priority: Priority = Field(default=Priority.MEDIUM)
    done: bool = False


class TodoUpdate(BaseModel):
    id: int
    title: str | None = Field(default=None, min_length=Measurement.MIN_TITLE_LENGTH)
    description: str | None = None
    priority: Priority | None = None
    done: bool | None = None
