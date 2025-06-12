# models/abstract_role.py

from abc import ABC, abstractmethod

class AbstractRole(ABC):
    def __init__(self, _id: int, full_name: str, email: str,
                 password_hash: str, created_at: str):
        self._id = _id
        self._full_name = full_name
        self._email = email
        self._password_hash = password_hash
        self._created_at = created_at

    def get_profile(self) -> dict:
        """
        Return a dictionary of the common profile fields.
        """
        return {
            "id":           self._id,
            "full_name":    self._full_name,
            "email":        self._email,
            "created_at":   self._created_at,
        }

    def update_profile(self, **kwargs) -> None:
        """
        Update any of the private fields (_id, _full_name, _email, _password_hash, _created_at)
        by passing them as keyword args. E.g. update_profile(full_name="New Name").
        """
        for field, val in kwargs.items():
            private_attr = f"_{field}"
            if hasattr(self, private_attr):
                setattr(self, private_attr, val)
