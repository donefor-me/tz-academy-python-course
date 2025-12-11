# * Yêu cầu:
#   * a. Dùng vòng lặp + unpacking tuple để in ra danh sách học viên theo format
#     ```text
#         SV01 - Nguyen Van A (20)
#         SV02 - Tran Thi B (21)
#         ...
#     ```
#   * b. Tạo một list mới `python_scores` chỉ chứa tuple `(student_id, name, python_score)`
#   * c. Tìm học viên có điểm Python cao nhất từ `python_scores` và in ra: `Top Python: <name> - <score>`
#   * d. Thêm môn mới `"database"` vào `courses` (dùng set) và gán tạm điểm `database = 0` cho tất cả sinh viên trong `scores`

students = [
    ("SV01", "Nguyen Van A", 20),
    ("SV02", "Tran Thi B", 21),
    ("SV03", "Le Van C", 19),
]

scores = {
    "SV01": {"math": 8.0, "python": 7.5},
    "SV02": {"math": 6.5, "python": 8.5},
    "SV03": {"math": 9.0, "python": 9.5},
}

courses = {"math", "python"}

python_scores: list[tuple[str, str, float]] = []


# a
def exercise_a() -> None:
    print("- a")
    for student in students:
        student_id, student_name, age = student
        print(f"{student_id} - {student_name} ({age})")


# b
def exercise_b() -> None:
    print("- b")
    try:
        for student in students:
            student_id, student_name, _ = student
            python_score = scores[student_id]["python"]
            python_scores.append((student_id, student_name, python_score))
    except KeyError:
        pass
    print(python_scores)


# c
def exercise_c() -> None:
    print("- c")
    _, student_name, python_score = python_scores[0]
    max_score = dict(
        name=student_name,
        score=python_score,
    )
    for python_score in python_scores:
        _, name, score = python_score
        if score >= max_score["score"]:
            max_score["name"] = name
            max_score["score"] = score

    print(max_score)


# d
def exercise_d() -> None:
    print("- d")
    courses_set = set(courses)
    courses_set.add("database")
    for student in scores.values():
        student["database"] = 0

    print(courses_set)
    print(scores)


def main():
    exercise_a()
    exercise_b()
    exercise_c()
    exercise_d()


if __name__ == "__main__":
    main()
