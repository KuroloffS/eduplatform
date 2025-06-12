import csv
from typing import List, Dict

def export_to_csv(data: List[Dict], filepath: str) -> None:
    """
    Given a list of dicts (all with same keys), write to CSV.
    """
    if not data:
        return
    with open(filepath, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(data[0].keys()))
        writer.writeheader()
        writer.writerows(data)
