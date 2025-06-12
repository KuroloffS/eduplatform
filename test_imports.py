from models.user import User
from models.role_enum import Role

u = User(1, "Alice", "a@b.com", "h", "2025-06-11", role=Role.STUDENT)
print(u.get_profile())
# → {'id': 1, 'full_name': 'Alice', 'email': 'alice@example.com',
#    'created_at': '2025-06-11', 'role': 'Student'}
