students = [["Alice", 85], ["Bob", 32], ["Charlie", 45]]
with open("result.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Marks"])
    writer.writerows(students)

with open("result.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row["Marks"]) >= 35:
            print(row)
