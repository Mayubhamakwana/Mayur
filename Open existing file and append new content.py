file_name = "file2.txt"
with open(file_name, "a") as f:
    f.write("\nAnother appended line.")

with open(file_name, "r") as f:
    print(f.read())
