# services/user_service.py

from models.user import User
from models.role_enum import Role
from services.base import dm
import hashlib
from datetime import datetime

class UserService:
    @staticmethod
    def register(full_name: str, email: str, password: str, role: Role) -> int:
        # 1. Ensure email is unique
        if any(u.email == email for u in dm.list_users()):
            raise ValueError(f"Email {email} already in use.")
        # 2. Hash the password
        pw_hash = hashlib.sha256(password.encode()).hexdigest()
        # 3. Create User
        now = datetime.now().isoformat()
        user = User(_id=None, full_name=full_name,
                    email=email, password_hash=pw_hash,
                    created_at=now, role=role)
        # 4. Store and return the new ID
        return dm.add_user(user)

    @staticmethod
    def authenticate(email: str, password: str) -> User | None:
        # 1. find user by email
        user = next((u for u in dm.list_users() if u.email == email), None)
        if not user:
            return None
        # 2. re-hash password and compare
        pw_hash = hashlib.sha256(password.encode()).hexdigest()
        if user.password_hash != pw_hash:
            return None
        # 3. return user or None
        return user
        pass

    @staticmethod
    def delete_user(user_id: int) -> bool:
        # 1. Fetch user to check if exists
        user = dm.get_user(user_id)
        if not user:
            raise ValueError(f"User with ID {user_id} does not exist.")
        # 2. Check if user is an Admin
        if user.role != Role.ADMIN:
            raise PermissionError("Only Admins can delete users.")
        # 3. Remove user from DataManager
        # only Admins allowed — check current user’s role externally
        return dm.remove_user(user_id)
