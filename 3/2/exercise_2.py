from student_model import Student
import re


def _is_valid_decimal(string: str) -> bool:
    try:
        float(string)
        return True
    except ValueError:
        return False


def load_students_from_file(filename: str) -> list[Student]:
    students = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("File not found")
        return []
    except IOError:
        print("IO Error")
        return []

    for index, line in enumerate(lines):
        if index == 0 or not line.strip():
            continue

        line_as_array = line.strip().split(",")

        if len(line_as_array) != 3:
            continue
        try:
            name = line_as_array[0].strip()
            age = int(line_as_array[1].strip())
            score = float(line_as_array[2].strip())

            students.append(Student(name, int(age), float(score)))
        except ValueError:
            continue

    return students


def calc_avg_score(students: list[Student]) -> float:
    if not students:
        return -1
    return sum(student.score for student in students) / len(students)


def find_top_student(students: list[Student]) -> list[Student]:
    if not students:
        return []
    max_score = max(student.score for student in students)
    return [student for student in students if student.score == max_score]


def filter_failed(students: list[Student]) -> list[Student]:
    if not students:
        return []
    return [student for student in students if not student.is_passed_exam()]


def extract_student(students: list[Student]) -> str:
    if not students:
        return "No student"
    return "\n - ".join(s.__str__() for s in students)


def main() -> None:
    too_lazy_to_input = "1"
    right_path_to_txt = "3/2/students.txt"
    file_name = input(
        f"Enter file name (valid name is '{right_path_to_txt}') or just press '{too_lazy_to_input}': ")

    if file_name == too_lazy_to_input:
        file_name = right_path_to_txt

    students = load_students_from_file(file_name)
    print("student list:\n", extract_student(students))
    print("average score: ", calc_avg_score(students))
    print("top score: ", [student.__str__() for student in find_top_student(students)])
    print("failed student: ", [student.__str__() for student in filter_failed(students)])


if __name__ == "__main__":
    main()
