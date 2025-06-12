# storage/data_manager.py

from typing import Dict, List, Optional
from models.user       import User
from models.assignment import Assignment
from models.grade      import Grade
from models.schedule   import Schedule
from models.notification import Notification

class DataManager:
    """
    In-memory repositories for all domain entities.
    """
    def __init__(self):
        # key → object
        self.users:         Dict[int, User]         = {}
        self.assignments:   Dict[int, Assignment]   = {}
        self.grades:        Dict[int, Grade]        = {}
        self.schedules:     Dict[int, Schedule]     = {}
        self.notifications: Dict[int, Notification] = {}

        # simple counters for unique IDs
        self._counters = {
            "user": 0,
            "assignment": 0,
            "grade": 0,
            "schedule": 0,
            "notification": 0,
        }

    def _next_id(self, entity: str) -> int:
        self._counters[entity] += 1
        return self._counters[entity]
    def add_user(self, user: User) -> int:
        """
        Assigns an ID if none, stores the User, and returns its ID.
        """
        if user._id is None:
            user._id = self._next_id("user")
        self.users[user._id] = user
        return user._id

    def get_user(self, user_id: int) -> Optional[User]:
        return self.users.get(user_id)

    def list_users(self) -> List[User]:
        return list(self.users.values())

    def remove_user(self, user_id: int) -> bool:
        return self.users.pop(user_id, None) is not None    
    def add_assignment(self, assignment: Assignment) -> int:
        """Assigns an ID if needed, stores the Assignment, and returns its ID."""
        if assignment.id is None:
            assignment.id = self._next_id("assignment")
        self.assignments[assignment.id] = assignment
        return assignment.id
    def get_assignment(self, assignment_id: int) -> Optional[Assignment]:
        return self.assignments.get(assignment_id)  
    def list_assignments(self) -> List[Assignment]:
        return list(self.assignments.values())  
    def remove_assignment(self, assignment_id: int) -> bool:
        return self.assignments.pop(assignment_id, None) is not None  
      
    def add_grade(self, grade: Grade) -> int:
        if grade.id is None:
            grade.id = self._next_id("grade")
        self.grades[grade.id] = grade
        return grade.id

    def get_grade(self, grade_id: int) -> Optional[Grade]:
        return self.grades.get(grade_id)

    def list_grades(self) -> List[Grade]:
        return list(self.grades.values())

    def remove_grade(self, grade_id: int) -> bool:
        return self.grades.pop(grade_id, None) is not None

    # — Notifications CRUD —
    def add_notification(self, notif: Notification) -> int:
        if notif.id is None:
            notif.id = self._next_id("notification")
        self.notifications[notif.id] = notif
        return notif.id

    def get_notification(self, notif_id: int) -> Optional[Notification]:
        return self.notifications.get(notif_id)

    def list_notifications(self) -> List[Notification]:
        return list(self.notifications.values())

    def remove_notification(self, notif_id: int) -> bool:
        return self.notifications.pop(notif_id, None) is not None
     
# Create a single, shared DataManager instance
_data_manager = DataManager()

def get_data_manager() -> DataManager:
    """
    Return the singleton DataManager.
    """
    return _data_manager
