import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"
symbol = "${}#@!%^&*()[]-=_+"

all = lower + upper + number + symbol
lengthInput = input("How long should the password be?: ")

if lengthInput == "":
    length = 8
else: 
    if int(lengthInput) < 8:
        length = 8
    else:
        length = int(lengthInput)

password = "".join(random.sample(all, length))

print("Password: ", password)