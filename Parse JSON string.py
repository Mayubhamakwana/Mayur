import json

json_str = '{"name":"Alice","marks":85}'   # JSON string
data = json.loads(json_str)                # Convert to Python dict

for k, v in data.items():
    print(k, v)

