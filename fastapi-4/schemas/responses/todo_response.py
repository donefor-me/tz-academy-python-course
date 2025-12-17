from pydantic import BaseModel, ConfigDict
from core.enums import Priority


class TodoResponse(BaseModel):
    todo_id: int
    title: str
    description: str | None
    priority: Priority
    done: bool

    model_config = ConfigDict(from_attributes=True)
