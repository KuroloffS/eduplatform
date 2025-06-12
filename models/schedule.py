# models/schedule.py

class Schedule:
    def __init__(self, id=None, teacher_id=None, start_time=None,
                 end_time=None, subject=""):
        self.id = id
        self.teacher_id = teacher_id
        self.start_time = start_time
        self.end_time = end_time
        self.subject = subject

    def conflicts_with(self, other: "Schedule") -> bool:
        # stub for later: check for time overlap
        pass
