from models.user import User
from models.role_enum import Role

class Parent(User):
    def __init__(self, _id, full_name, email, password_hash, created_at, children_ids=None):
        super().__init__(_id, full_name, email, password_hash, created_at, role=Role.PARENT)
        self.children_ids = children_ids or []

    def view_child_progress(self, child_id: int) -> dict:
        """Stub: fetch and return a child’s profile/grades."""
        pass
