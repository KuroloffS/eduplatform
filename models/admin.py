from models.user import User
from models.role_enum import Role

class Admin(User):
    def __init__(self, _id, full_name, email, password_hash, created_at, permissions=None):
        super().__init__(_id, full_name, email, password_hash, created_at, role=Role.ADMIN)
        self.permissions = permissions or []

    def add_user(self, user: User) -> None:
        """Stub: add to DataManager."""
        pass

    def remove_user(self, user_id: int) -> None:
        """Stub: remove from DataManager."""
        pass

    def generate_report(self) -> str:
        """Stub: compile and return a summary report."""
        pass
