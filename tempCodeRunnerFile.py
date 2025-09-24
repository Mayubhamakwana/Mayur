roll = input("Enter roll number: ")
with open("students.csv", "r") as f:
    reader = csv.DictReader(f)