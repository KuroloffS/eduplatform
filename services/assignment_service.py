# services/assignment_service.py

from models.assignment import Assignment
from services.base import dm

class AssignmentService:
    @staticmethod
    def create(title: str, description: str, deadline: str) -> int:
        # 1. Instantiate
        inst = Assignment(id=None, title=title,
                          description=description, deadline=deadline)
        # 2. Store
        aid = dm.add_assignment(inst)
        # 3. (Optional) notify all students here via NotificationService
        return aid

    @staticmethod
    def submit(student_id: int, assignment_id: int, content: str) -> None:
        inst = dm.get_assignment(assignment_id)
        if inst is None:
            raise ValueError("Assignment not found")
        inst.add_submission(student_id, content)