import csv
from typing import Tuple


def load_to_csv(data: Tuple, filename: str) -> None:

    headers, rows = data
    # Write to CSV file
    with open(filename, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)
        writer.writerows(rows)

    print(f"Data successfully extracted and saved to {filename}")

    return
