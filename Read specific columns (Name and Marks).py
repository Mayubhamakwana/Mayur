import csv
with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['Name'], row['Marks'])
