from base_exception import BusinessException


class StudentNotFoundException(BusinessException):
    def __init__(self, student_id: int):
        super().__init__(
            message=f"Student {student_id} not found",
            error_code="STUDENT_NOT_FOUND",
            status_code=404,
            extra={"student_id": student_id},
        )


class StudentEmailAlreadyExistsException(BusinessException):
    def __init__(self, email: str):
        super().__init__(
            message="Email already exists",
            error_code="EMAIL_ALREADY_EXISTS",
            status_code=409,
            extra={"email": email},
        )


class InvalidStudentAgeException(BusinessException):
    def __init__(self, age: int):
        super().__init__(
            message="Age must be >= 18",
            error_code="INVALID_STUDENT_AGE",
            status_code=400,
            extra={"age": age},
        )
