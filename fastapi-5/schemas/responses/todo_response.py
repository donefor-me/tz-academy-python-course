from pydantic import BaseModel
from cores.enums import Priority


class TodoResponse(BaseModel):
    id: int
    title: str
    description: str | None
    priority: Priority
    done: bool

    class Config:
        from_attributes = True
