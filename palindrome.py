# Functions to get new strings
def reverseString(stringToReverse):
    global reversedString;
    
    reversedString = stringToReverse[::-1];


def parseString(stringToConvert):
    global parsedString;
    global alphanumerics;

    lowerCase = stringToConvert.lower();
    
    for char in lowerCase:
        if char in alphanumerics:
            parsedString += char;


# Variables to store
alphanumerics = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"];
parsedString = "";
reversedString = "";

# Execute
print("Welcome to the palindrome checker \n");

inputString = input("Enter a word: \n");

parseString(inputString);
if parsedString != "":
    reverseString(parsedString);
elif parsedString == "":
    print("\n Invalid Input: Please try again with alphabets or numbers. \n")
else:
    print("\n Parse Error: Please try again.")

# Handle results
if parsedString == reversedString:
    print("\n The word or sentence you have entered is a palindrome! \n");
elif parsedString != reversedString:
    print("\n The word or sentence you have entered is not a palindrome \n");
else:
    print("\n Check Error: Please try again. \n")
