from datetime import datetime
from enum import Enum, unique


@unique
class Status(Enum):
    TODO = 0
    DONE = 1


@unique
class ISO(str, Enum):
    YEAR_MONTH_DATE = "%Y-%m-%d"


ENCODING = "utf-8"
DELIMITER = ","


class Task:
    def __init__(self, task_id: int, description: str, due_date: datetime, status: int = Status.TODO.value):
        self.task_id = task_id
        self.description = description
        self.due_date = due_date
        self.status = status

    def is_overdue(self) -> bool:
        return self.status == Status.DONE and datetime.now() > self.due_date

    def __str__(self) -> str:
        due_str = self.due_date.strftime(ISO.YEAR_MONTH_DATE)

        return f"{self.task_id} | {self.description} | due date: {due_str} | Status: {Status(self.status).name}"

    def to_line(self) -> str:
        due_str = self.due_date.strftime(ISO.YEAR_MONTH_DATE)

        return str(self.task_id) + DELIMITER + self.description + DELIMITER + due_str + DELIMITER + str(
            Status(self.status).value
        ) + "\n"
