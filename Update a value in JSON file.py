import json
with open("employees.json","r") as f:
    data = json.load(f)
data[0]["salary"] = 55000
with open("employees.json","w") as f:
    json.dump(data,f)
