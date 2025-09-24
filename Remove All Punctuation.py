import string
text = "Hello, world! Python."
text = text.translate(str.maketrans('', '', string.punctuation))
print(text)
