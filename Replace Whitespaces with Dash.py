import re
text = "Hello World Python"
text = re.sub(r'\s+', '-', text)
print(text)
