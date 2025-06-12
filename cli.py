# cli.py
from models.user import User

def main():
    user = User(_id=1, full_name="Test", email="a@b.com",
                password_hash="xxx", created_at="2025-06-11", role=None)
    print(user.get_profile())

if __name__ == "__main__":
    main()
