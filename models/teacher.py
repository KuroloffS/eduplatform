from models.user import User
from models.role_enum import Role

class Teacher(User):
    def __init__(self, _id, full_name, email, password_hash, created_at,
                 subjects=None, classes=None):
        super().__init__(_id, full_name, email, password_hash, created_at, role=Role.TEACHER)
        self.subjects = subjects or []  # e.g. ["Math", "Physics"]
        self.classes = classes or []    # e.g. ["9A", "10B"]

    def create_assignment(self, title: str, description: str, deadline: str):
        """Stub: return an Assignment instance or ID."""
        pass

    def grade_assignment(self, student_id: int, assignment_id: int, score: float) -> None:
        """Record a grade for a student’s submission."""
        pass
