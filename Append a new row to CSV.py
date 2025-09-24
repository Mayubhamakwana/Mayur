import csv

# Open CSV file in append mode
with open("students.csv", "a", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["David", 88])  # Appends a new row
