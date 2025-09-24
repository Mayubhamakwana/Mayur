with open("file2.txt", "a") as f:
    f.write("\nAppending a new line.")

with open("file2.txt", "r") as f:
    print(f.read())
