# Program 2
def display_name(name):
    if name:  # if name is not empty
        print("Your name is:", name)
    else:
        print("No name provided")

# Input from user
user_name = input("Enter your name: ")
display_name(user_name)
