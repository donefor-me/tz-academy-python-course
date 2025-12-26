from exceptions.base_exception import BusinessException


class TodoNotFoundException(BusinessException):
    def __init__(self, todo_id: int):
        super().__init__(
            message=f"Todo with id {todo_id} not found",
            error_code="TODO_NOT_FOUND",
            status_code=404,
            extra={"todo_id": todo_id},
        )


class TodoTitleAlreadyExistsException(BusinessException):
    def __init__(self, title: str):
        super().__init__(
            message=f"Todo title '{title}' already exists",
            error_code="TODO_TITLE_ALREADY_EXISTS",
            status_code=409,
            extra={"title": title},
        )


class InvalidTodoPriorityException(BusinessException):
    def __init__(self, priority: int):
        super().__init__(
            message="Priority must be between 1 and 5",
            error_code="INVALID_TODO_PRIORITY",
            status_code=400,
            extra={"priority": priority},
        )
