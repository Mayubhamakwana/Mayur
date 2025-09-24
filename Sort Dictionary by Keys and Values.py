students = {"Alice": 85, "Bob": 72, "Charlie": 90}
sorted_by_key = dict(sorted(students.items()))
sorted_by_value = dict(sorted(students.items(), key=lambda x: x[1]))
print("By Key:", sorted_by_key)
print("By Value:", sorted_by_value)
