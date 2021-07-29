import re

id = input()
password = input()
x = re.search("^.{3,32}#[0-9]{4}", id)
y = re.search("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$", password)
if x:
    if y:
        print("Welcome to Discord")
    else:
        print("Invalid password or username")
else:
    print("Invalid password or username")