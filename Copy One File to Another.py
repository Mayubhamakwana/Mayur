with open("file2.txt", "r") as src:
    content = src.read()

with open("file_copy.txt", "w") as dst:
    dst.write(content)
