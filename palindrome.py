import re

# Functions to get new strings
def reverseString(stringToReverse):
    global reversedString;
    
    reversedString = stringToReverse[::-1];


def parseString(stringToConvert):
    global parsedString;

    lowerCase = stringToConvert.lower();
    
    parsedString = ''.join(re.findall(r'[a-z0-9]', lowerCase))


# Variables to store
parsedString = "";
reversedString = "";

# Execute
print("Welcome to the palindrome checker \n");

inputString = input("Enter a word: \n");

parseString(inputString);
if len(parsedString) > 0:
    reverseString(parsedString);
else:
    print("\n Invalid Input: Please try again with alphabets or numbers. \n")

# Handle results
if parsedString == reversedString:
    print("\n The word or sentence you have entered is a palindrome! \n");
else:
    print("\n The word or sentence you have entered is not a palindrome \n");
