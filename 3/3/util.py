from task_model import Task, Status, DELIMITER, ENCODING, ISO
from datetime import datetime
import os
import tempfile


def _format_date(date_str: str, _format: str = ISO.YEAR_MONTH_DATE) -> datetime:
    try:
        return datetime.strptime(date_str, _format)
    except ValueError:
        raise ValueError(f"{date_str} is not a valid date")


def get_task_from_file(file_path: str) -> list[Task]:
    tasks = []
    try:
        with open(file_path, "r", encoding=ENCODING) as file:
            for line in file:
                if not line.strip():
                    continue
                line_as_arr = line.strip().split(DELIMITER)
                task_id = int(line_as_arr[0])
                description = line_as_arr[1].strip()
                due_date = line_as_arr[2].strip()
                status = int(line_as_arr[3])
                tasks.append(Task(task_id, description, _format_date(due_date), status))
            return tasks
    except FileNotFoundError:
        print("File not found")
        return []
    except IOError:
        print("IO Error")
        return []
    except ValueError as e:
        print("ValueError")
        raise e


def print_all_task(task_list: list[Task]) -> None:
    if not task_list:
        print("No tasks found")
        return
    for task in task_list:
        print(task.__str__())


def print_overdue_task(task_list: list[Task]) -> None:
    if not task_list:
        print("No tasks found")
        return
    for t in [task for task in task_list if bool(task.is_overdue())]:
        print(f"{t.description} (Due date: {t.due_date})")


def change_status_and_write(file_path: str, new_task: Task) -> bool:
    found = False
    temp_fd, temp_path = tempfile.mkstemp()


    try:
        with open(file_path, "r", encoding=ENCODING) as src_file, \
                open(f"{temp_fd}{datetime.now()}", "w", encoding=ENCODING) as dst:

            for line in src_file:
                if not line.strip():
                    dst.write(line)
                    continue

                parts = line.strip().split(DELIMITER)
                if int(parts[0]) == new_task.task_id:
                    dst.write(new_task.to_line())
                    found = True
                else:
                    dst.write(line)

        if not found:
            with open(temp_path, "a", encoding=ENCODING) as dst:
                dst.write(new_task.to_line() + "\n")

        os.replace(temp_path, file_path)
        return True
    except FileNotFoundError:
        os.remove(temp_path)
        return False
    except OSError:
        os.remove(temp_path)
        return False
    finally:
        os.remove(temp_path)


def add_tasks_to_file(file_path: str, task_list: list[Task]) -> bool:
    try:
        with open(file_path, "a", encoding=ENCODING) as file:
            content = file.read()
            need_newline = bool(content) and not content.endswith("\n")
            for task in task_list:
                if need_newline:
                    file.write("\n")
                file.write(task.to_line())

        return True
    except FileNotFoundError:
        return False
    except IOError:
        return False


def create_new_task(task_id: int, description: str, due_date: str, status: Status = Status.TODO) -> Task | None:
    try:
        _due_date = datetime.strptime(str(due_date), "%Y-%m-%d")
        return Task(task_id, description, _due_date, status)
    except ValueError:
        return None


def get_lastest_task_id(task_list: list[Task]) -> int:
    if not task_list:
        return 1
    return task_list[-1].task_id + 1
