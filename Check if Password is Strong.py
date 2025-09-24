import re
pwd = input("Enter password: ")
pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$'
print("Strong" if re.match(pattern, pwd) else "Weak")
