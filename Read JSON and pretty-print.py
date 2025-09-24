import json

employees = [
    {"name": "Alice", "salary": 50000},
    {"name": "Bob", "salary": 60000}
]

with open("employees.json", "w") as f:
    json.dump(employees, f, indent=4)
