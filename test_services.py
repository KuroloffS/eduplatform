# test_services.py
from services.user_service import UserService
from services.assignment_service import AssignmentService
from services.grading_service import GradingService
from services.notification_service import NotificationService
from models.role_enum import Role
from datetime import datetime
from storage.data_manager import get_data_manager
dm = get_data_manager()
# 1. Register a teacher and a student
t_id = UserService.register("Mr. T", "t@x.com", "pass", Role.TEACHER)
s_id = UserService.register("Stu",  "s@x.com", "pass", Role.STUDENT)

# 2. Teacher creates an assignment
a_id = AssignmentService.create("HW1", "Do problems", "2025-06-20")

# 3. Student submits
AssignmentService.submit(s_id, a_id, "My answers")

# 4. Teacher grades
g_id = GradingService.grade(s_id, a_id, 95.0, graded_by=t_id, graded_at=str(datetime.now()))

# 5. Notify student
NotificationService.notify(s_id, "Your grade is ready")

# 6. Print results
print("Users:", [u.get_profile() for u in dm.list_users()])
print("Assignments:", [a.title for a in dm.list_assignments()])
print("Grades:", [vars(g) for g in dm.list_grades()])
print("Notifs:", [vars(n) for n in dm.list_notifications()])
