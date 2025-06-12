# models/role_enum.py

from enum import Enum

class Role(Enum):
    ADMIN   = "Admin"
    TEACHER = "Teacher"
    STUDENT = "Student"
    PARENT  = "Parent"
