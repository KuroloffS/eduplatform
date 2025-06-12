# exports/sql_exporter.py

from typing import List, Dict, Any, Optional
from datetime import datetime

def export_to_sql(
    table: str,
    data: List[Dict[str, Any]],
    filepath: str,
    type_map: Optional[Dict[type, str]] = None
) -> None:
    if not data:
        return

    # 1) Prepare type mapping
    default_map = {
        int:      "INTEGER",
        float:    "REAL",
        str:      "TEXT",
        bool:     "BOOLEAN",
        datetime: "TIMESTAMP"
    }
    type_map = {**default_map, **(type_map or {})}

    cols = list(data[0].keys())

    def infer_type(col: str) -> str:
        for row in data:
            v = row.get(col)
            if v is not None:
                return type_map.get(type(v), "TEXT")
        return "TEXT"

    # 2) Build CREATE TABLE
    col_defs = ",\n  ".join(f"`{c}` {infer_type(c)}" for c in cols)
    create_stmt = f"CREATE TABLE `{table}` (\n  {col_defs}\n);\n\n"

    # 3) Value-escaping helper
    def escape(val: Any) -> str:
        if val is None:
            return "NULL"
        if isinstance(val, str):
            return "'" + val.replace("'", "''") + "'"
        if isinstance(val, bool):
            return 'TRUE' if val else 'FALSE'
        if isinstance(val, datetime):
            return "'" + val.isoformat() + "'"
        return str(val)

    # 4) Write to file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(create_stmt)
        for row in data:
            cols_esc = ", ".join(f"`{c}`" for c in cols)
            vals     = ", ".join(escape(row[c]) for c in cols)
            f.write(f"INSERT INTO `{table}` ({cols_esc}) VALUES ({vals});\n")
