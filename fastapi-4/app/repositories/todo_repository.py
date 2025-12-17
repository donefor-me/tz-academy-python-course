from app.models.todo_model import TodoModel
from typing import List, Tuple


class TodoRepository:
    """In-memory repository for Todo items using a class-level list.

    All methods are class methods (@classmethod) so the repository can be used
    without creating an instance. Intended for testing or simple applications.
    """

    _todos: List[TodoModel] = []
    _id_counter: int = 1

    def __init__(self):
        pass

    @classmethod
    def set_global_id(cls, id_counter: int) -> None:
        """Return a tuple of all todos (immutable)."""
        cls._id_counter = id_counter

    @classmethod
    def get_todos(cls) -> Tuple[TodoModel, ...]:
        """Return a tuple of all todos (immutable)."""
        return tuple(cls._todos)

    @classmethod
    def get_id_counter(cls) -> int:
        """Return the current value of the next ID counter."""
        return cls._id_counter

    @classmethod
    def next_id(cls) -> int:
        """Generate and return the next available todo ID (auto-increments)."""

        current_id = cls._id_counter
        cls._id_counter += 1
        return current_id

    @classmethod
    def find_by_id(cls, todo_id: int) -> TodoModel | None:
        """Find a todo by its ID.

        Returns:
            TodoModel if found, otherwise None.
        """
        return next((t for t in cls._todos if t.todo_id == todo_id), None)

    @classmethod
    def add(cls, todo: TodoModel) -> None:
        """
        Returns: None
        """
        cls._todos.append(todo)

    @classmethod
    def update(cls, todo: TodoModel) -> None:
        """Replace an existing todo with the given one (identified by todo_id).

        Raises:
            ValueError: If no todo with the given todo_id exists.
        """
        for index, existing in enumerate(cls._todos):
            if existing.todo_id == todo.todo_id:
                cls._todos[index] = todo
                return

    @classmethod
    def delete(cls, todo_id: int) -> None:
        """Remove a todo from the repository.

        Raises:
            ValueError: If the todo is not found in the list.
        """
        for i, existing in enumerate(cls._todos):
            if existing.todo_id == todo_id:
                cls._todos.remove(existing)
                return
