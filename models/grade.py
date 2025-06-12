# models/grade.py

class Grade:
    def __init__(self, id=None, student_id=None, assignment_id=None,
                 score=None, graded_by=None, graded_at=None):
        self.id = id
        self.student_id = student_id
        self.assignment_id = assignment_id
        self.score = score
        self.graded_by = graded_by
        self.graded_at = graded_at
