from enum import Enum
from util import get_task_from_file, print_all_task, print_overdue_task, get_lastest_task_id, create_new_task, \
    add_tasks_to_file, change_status_and_write

FILE_PATH = "3/3/tasks.txt"


class MenuOption(Enum):
    VIEW_ALL = 1
    VIEW_OVERDUE = 2
    ADD_NEW = 3
    MARK_DONE = 4
    EXIT = 5


MENUS = {
    MenuOption.VIEW_ALL: "Xem tất cả task",
    MenuOption.VIEW_OVERDUE: "Xem các task quá hạn",
    MenuOption.ADD_NEW: "Thêm task mới",
    MenuOption.MARK_DONE: "Đánh dấu task là done",
    MenuOption.EXIT: "Thoát",
}


def execute_terminal() -> None:
    tasks = get_task_from_file(FILE_PATH)
    while True:
        print("Menu list: ")
        for option in MENUS:
            print(f"{option.value}: {MENUS[option]}")

        raw_input = input("\n> ")

        try:
            input_as_int = int(raw_input)
        except ValueError:
            print("Invalid input")
            continue

        if input_as_int == MenuOption.EXIT.value:
            print("Bye")
            break

        try:
            input_as_menu = MenuOption(input_as_int).value
        except ValueError:
            print("Invalid input")
            continue

        if input_as_menu == MenuOption.VIEW_ALL.value:
            print_all_task(tasks)
            continue

        if input_as_menu == MenuOption.VIEW_OVERDUE.value:
            print_overdue_task(tasks)
            continue

        if input_as_menu == MenuOption.ADD_NEW.value:
            task_description = input("Task description: ") # TODO: Add name validator: max length, restrict words ...
            task_due_date = input("Task due date: ") # TODO: Add date validator: before now, valid date ...
            new_task = create_new_task(get_lastest_task_id(tasks), task_description, task_due_date)
            add_success = add_tasks_to_file(FILE_PATH, [new_task])
            if add_success:
                tasks = get_task_from_file(FILE_PATH)
                print("added new task")
            else:
                print("failed to add new task")
            continue

        if input_as_menu == MenuOption.MARK_DONE.value:
            print("pick a task id to mark done")
            print_all_task(tasks)
            task_id = input(">: ")
            try:
                task_id = int(task_id)
            except ValueError:
                print("Invalid input")
            if not task_id in [task.task_id for task in tasks]:
                print("failed to mark task")
            tasks_done = [task for task in tasks if task.task_id == task_id][0]  # use filter instead
            change_status_and_write(FILE_PATH, tasks_done)
            tasks = get_task_from_file(FILE_PATH)
            continue


def main() -> None:
    execute_terminal()


if __name__ == "__main__":
    main()
