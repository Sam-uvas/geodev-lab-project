import csv

def inspect_column(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    values = []
    non_numeric = 0

    for row in rows:
        raw = (row[column] or "").strip()

        if raw == "":
            continue

        try:
            values.append(float(raw))
        except ValueError:
            non_numeric += 1

    if not values:
        return {"Message": "No valid numeric values found"}

    return {
        "Smallest": min(values),
        "Largest": max(values),
        "Count": len(values),
        "Average": sum(values) / len(values),
        "Non-numeric values": non_numeric
    }


capacity_stats = inspect_column("renewable_energy.csv", "MEGAWATT")
print("Renewable energy capacity statistics:")
print(capacity_stats)

area_stats = inspect_column("renewable_energy.csv", "Shape_Area")
print("Project area statistics:")
print(area_stats)