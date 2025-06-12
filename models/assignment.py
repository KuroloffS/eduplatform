# models/assignment.py

class Assignment:
    def __init__(self, id=None, title="", description="", deadline=""):
        self.id = id
        self.title = title
        self.description = description
        self.deadline = deadline
        self.submissions = {}  # student_id → content
        self.grades = {}       # student_id → score

    def add_submission(self, student_id: int, content: str) -> None:
        """Record a student’s submission."""
        self.submissions[student_id] = content

    def set_grade(self, student_id: int, score: float) -> None:
        """Record a grade for a student’s submission."""
        self.grades[student_id] = score
