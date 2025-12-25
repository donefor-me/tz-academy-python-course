from typing import Optional


class TodoModel:
    def __init__(
        self,
        todo_id: int,
        title: str,
        description: Optional[str],
        priority: int,
        done: bool = False,
    ):
        self.todo_id = todo_id
        self.title = title
        self.description = description
        self.priority = priority
        self.done = done
