with open("file2.txt", "w") as f:
    f.write("This is some sample content.\nSecond line.")

with open("file2.txt", "r") as f:
    print(f.read())
