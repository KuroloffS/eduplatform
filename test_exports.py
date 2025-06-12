# test_exports.py

from storage.data_manager import get_data_manager
from exports.csv_exporter    import export_to_csv
from exports.excel_exporter  import export_to_excel
from exports.sql_exporter    import export_to_sql
from models.user             import User
from models.role_enum        import Role

dm = get_data_manager()

# seed a couple users
dm.add_user(User(None, "Alice", "a@b.com", "h", "2025-06-11", Role.STUDENT))
dm.add_user(User(None, "Bob",   "b@c.com", "h", "2025-06-11", Role.TEACHER))

# extract profiles as dicts
dataset = [u.get_profile() for u in dm.list_users()]

export_to_csv(dataset,   "users.csv")
export_to_excel(dataset, "users.xlsx")
export_to_sql("users",   dataset, "users.sql")

print("Wrote users.csv, users.xlsx, users.sql")
