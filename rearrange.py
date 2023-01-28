# Initialize the program
import random

inputString = ""
parsedString = ""
newString = ""
output = ""
factorial = 1
permutations = []


# Get and format user input
def getInput():
    global inputString
    global parsedString

    inputString = input("Enter a string (without spaces): \n")
    inputString = inputString.strip()
    words = inputString.split()

    # Only accept valid string
    if words[0].isalpha():
        parsedString = words[0].lower()
    else:
        print("Error, please use alphabetic characters only")


# Get permutations (High time complexity, decent space complexity)
def shuffleString():
    global parsedString
    global permutations
    global newString
    global output

    newString = ''.join(random.sample(parsedString, len(parsedString)))

    # Only accept valid string
    if newString not in permutations:
        print(newString)
        output = newString
        permutations.append(newString)
    else:
        return


# Get the total number of permutations possible
def getFactorial():
    global parsedString
    global factorial

    wordLength = len(parsedString)

    for i in range(1, wordLength+1):
        factorial = factorial*i


# Execute all the functions as needed
def runApp():
    global parsedString
    global newString
    global output

    while parsedString == "":
        getInput()
    else:
        print("Your string is:", parsedString)

    getFactorial()
    print("Total permutations:", factorial)

    while factorial > len(permutations):
        shuffleString()
    # else:
    #     print("\nRESULTS:")
    #     for i in range(len(permutations)):
    #         print(permutations[i])


# Run the program (duh)
print("Welcome to the permuting machine!")
print("This is a basic project made in 1 hour by Gyryk, If it's slow that's because it was never optimized for speed\n")
runApp()
print("Thanks for using this program")
