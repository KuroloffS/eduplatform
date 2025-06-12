# services/grading_service.py

from models.grade import Grade
from services.base import dm

class GradingService:
    @staticmethod
    def grade(student_id: int, assignment_id: int,
              score: float, graded_by: int, graded_at: str) -> int:
        # 1. Create Grade record
        gr = Grade(id=None, student_id=student_id,
                   assignment_id=assignment_id,
                   score=score, graded_by=graded_by,
                   graded_at=graded_at)
        gid = dm.add_grade(gr)
        # 2. Update the Assignment’s own grade map
        assignment = dm.get_assignment(assignment_id)
        if assignment:
            assignment.set_grade(student_id, score)
        return gid

    @staticmethod
    def stats_for_student(student_id: int) -> dict:
        # compute average/min/max from dm.list_grades()
        grades = dm.list_grades()
        student_grades = [g for g in grades if g.student_id == student_id]
        if not student_grades:
            return {"average": 0, "min": 0, "max": 0}
        scores = [g.score for g in student_grades]
        return {
            "average": sum(scores) / len(scores),
            "min": min(scores),
            "max": max(scores)
        }
    
