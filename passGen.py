import random
import string

all = string.ascii_letters + string.digits + '${}#@!%&()-=_+[]'

lengthInput = input("How long should the password be?: ")

if lengthInput == "":
    length = 8
else: 
    try:
        length = int(lengthInput)
        if length < 8:
            print('Length too short, setting to 8')
            length = 8
    except ValueError:
        print('Invalid input')
        exit()
        
password = "".join(random.choices(all, k=length))

print("New Password: ", password)
