import re
para = "Hello world. Python is fun! Let's code."
sentences = re.split(r'[.!?]\s*', para)
sentences = [s for s in sentences if s]
print(sentences)
