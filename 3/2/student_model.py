class Student:
    PASSED_SCORE = 5

    def __init__(self, name: str, age: int, score: float) -> None:
        self.name = name
        self.age = age
        self.score = score

    def is_passed_exam(self) -> bool:
        return self.score >= Student.PASSED_SCORE

    def __str__(self) -> str:
        return f'Student {self.name}, age: {self.age}, score: {self.score}'
