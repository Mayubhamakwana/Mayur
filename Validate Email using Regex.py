import re
email = input("Enter email: ")
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
print("Valid" if re.match(pattern, email) else "Invalid")
