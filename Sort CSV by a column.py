import csv
with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    sorted_data = sorted(reader, key=lambda x: int(x['Age']))
print(sorted_data)
