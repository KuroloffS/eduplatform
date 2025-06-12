from models.user import User
from models.role_enum import Role

class Student(User):
    def __init__(self, _id, full_name, email, password_hash, created_at,
                 grade: str = "", subjects=None):
        super().__init__(_id, full_name, email, password_hash, created_at, role=Role.STUDENT)
        self.grade = grade
        self.subjects = subjects or {}
        self.assignments = []   # list of assignment IDs
        self.grades = {}        # assignment_id → score

    def submit_assignment(self, assignment_id: int, content: str) -> None:
        """Record a student’s submission."""
        pass

    def calculate_average_grade(self) -> float:
        """Compute the student’s average over self.grades."""
        pass
