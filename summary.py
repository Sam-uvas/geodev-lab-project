import csv


def read_rows(filename):
    with open(filename, encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        return list(reader)


def clean_values(rows, column):
    values = []

    for row in rows:
        raw = (row[column] or "").strip()

        if raw == "":
            continue

        try:
            values.append(float(raw))
        except ValueError:
            continue

    return values


def summarise(values):
    if len(values) == 0:
        return {
            "count": 0,
            "smallest": None,
            "largest": None,
            "average": None
        }

    return {
        "count": len(values),
        "smallest": min(values),
        "largest": max(values),
        "average": sum(values) / len(values)
    }


def summarise_all(filename, columns):
    rows = read_rows(filename)
    report = {}

    for column in columns:
        values = clean_values(rows, column)
        report[column] = summarise(values)

    return report


report = summarise_all(
    "renewable_energy.csv",
    ["MEGAWATT", "Shape_Area"]
)

for column, stats in report.items():
    print(
        f"{column} -> "
        f"count: {stats['count']}, "
        f"smallest: {stats['smallest']}, "
        f"largest: {stats['largest']}, "
        f"average: {stats['average']}"
    )