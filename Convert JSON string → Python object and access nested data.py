json_str = '{"company": {"employee": {"name":"Alice","salary":50000}}}'
data = json.loads(json_str)
print(data["company"]["employee"]["name"])
