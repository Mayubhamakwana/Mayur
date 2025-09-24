with open("students.csv", "r") as f:
    reader = list(csv.reader(f))
    rows = len(reader)
    cols = len(reader[0])
print("Rows:", rows, "Columns:", cols)
