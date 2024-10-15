import csv


def load_to_csv(data, filename):

    headers, rows = data
    # Write to CSV file
    with open(filename, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)
        writer.writerows(rows)

    print(f"Data successfully extracted and saved to {filename}")
