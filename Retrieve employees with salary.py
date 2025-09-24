import json
with open("employees.json","r") as f:
    data = json.load(f)
for emp in data:
    if emp["salary"] > 50000:
        print(emp)
