# models/user.py

from models.abstract_role import AbstractRole
from models.role_enum import Role

class User(AbstractRole):
    def __init__(self, _id, full_name, email, password_hash, created_at, role: Role):
        super().__init__(_id, full_name, email, password_hash, created_at)
        self.role = role
        self._notifications = []
        
    @property
    def email(self) -> str:
        """Public getter for the user’s email."""
        return self._email

    @property
    def id(self) -> int:
        """Public getter for the user’s ID."""
        return self._id
    
    def add_notification(self, message: str) -> None:
        notif_id = len(self._notifications) + 1
        self._notifications.append({"id": notif_id, "msg": message, "read": False})


    def view_notifications(self) -> list:
        return list(self._notifications)


    def delete_notification(self, notif_id: int) -> None:
        self._notifications = [
            n for n in self._notifications if n["id"] != notif_id
        ]

    def get_profile(self) -> dict:
        data = super().get_profile()
        data["role"] = self.role.value
        return data
    
    def update_profile(self, **kwargs) -> None:
        super().update_profile(**kwargs)
