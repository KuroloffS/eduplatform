from openpyxl import Workbook
from typing import List, Dict

def export_to_excel(data: List[Dict], filepath: str, sheet_name: str = "Sheet1") -> None:
    """
    Given a list of dicts, write to an XLSX file.
    """
    wb = Workbook()
    ws = wb.active
    ws.title = sheet_name

    if not data:
        wb.save(filepath)
        return

    headers = list(data[0].keys())
    ws.append(headers)
    for row in data:
        ws.append([row[h] for h in headers])
    wb.save(filepath)
