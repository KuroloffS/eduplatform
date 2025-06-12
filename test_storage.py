# test_storage.py

from models.user          import User
from models.role_enum     import Role
from storage.data_manager import get_data_manager

dm = get_data_manager()

u = User(None, "Bob", "bob@example.com", "h", "2025-06-11", role=Role.PARENT)
uid = dm.add_user(u)
print("Added user ID:", uid)
print("Fetched:", dm.get_user(uid).get_profile())
print("All users:", [user.get_profile() for user in dm.list_users()])
print("Removed?", dm.remove_user(uid))
print("Now:", dm.list_users())
