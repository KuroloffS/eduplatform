# services/schedule_service.py

from models.schedule import Schedule
from services.base import dm

class ScheduleService:
    @staticmethod
    def add_lesson(teacher_id: int, start_time: str,
                   end_time: str, subject: str) -> int:
        # 1. create Schedule(None, teacher_id, start, end, subject)
        # 2. check conflicts: for each existing schedule for that teacher
        # 3. if no conflict, dm.add_schedule(...)
        pass

    @staticmethod
    def remove_lesson(schedule_id: int) -> bool:
        return dm.remove_schedule(schedule_id)
