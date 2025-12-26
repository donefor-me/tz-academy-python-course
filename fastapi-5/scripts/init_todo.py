from app.models.todo_model import TodoModel
from app.repositories.todo_repository import TodoRepository
from cores.database import SessionLocal


def init_todo() -> None:
    tasks_data = [
        {"title": "Nghiên cứu thị trường", "priority": 1, "done": False},
        {"title": "Gửi email nhắc nhở", "priority": 2, "done": True},
        {"title": "Sắp xếp thư mục Drive", "priority": 3, "done": False},
    ]
    db = SessionLocal()
    repo = TodoRepository()
    try:
        todo_objs = [TodoModel(**data) for data in tasks_data]
        repo.bulk_create(db, todo_objs)
        db.commit()
        print(f"Successfully initialized {len(todo_objs)} tasks.")
    except Exception as e:
        db.rollback()
        print(f"Error during initialization: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    init_todo()
