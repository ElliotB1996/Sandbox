"""Elliot Blair"""

name = input("What is your name?")

while name == "" or name == " ":
    print("Name must not be blank")
    name = input("What is your name?")

print(name)


