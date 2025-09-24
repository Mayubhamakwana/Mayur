import csv
roll = input("Enter roll number: ")
with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['Roll'] == roll:
            print(row)
