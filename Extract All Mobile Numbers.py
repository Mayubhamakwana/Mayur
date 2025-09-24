import re
text = "Call me at 9876543210 or 9123456789"
numbers = re.findall(r'\b\d{10}\b', text)
print(numbers)
