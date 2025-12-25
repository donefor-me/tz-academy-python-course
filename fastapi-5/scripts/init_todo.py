from app.models.todo_model import TodoModel
from app.repositories.todo_repository import TodoRepository


def init_todo() -> None:
    todo_1 = TodoModel(
        todo_id=TodoRepository.next_id(),
        title="Nghiên cứu thị trường",
        description="Tìm hiểu xu hướng mới nhất trong lĩnh vực AI",
        priority=1,
        done=False,
    )

    todo_2 = TodoModel(
        todo_id=TodoRepository.next_id(),
        title="Gửi email nhắc nhở",
        description="Nhắc nhở đội ngũ về deadline sắp tới",
        priority=2,
        done=True,
    )

    todo_3 = TodoModel(
        todo_id=TodoRepository.next_id(),
        title="Sắp xếp thư mục Drive",
        description=None,
        priority=3,
        done=False,
    )

    tasks = [todo_1, todo_2, todo_3]

    for task in tasks:
        TodoRepository.add(task)
