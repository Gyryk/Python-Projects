# Imports
import random

# Probability
heads = 50983
tails = 49000
edges = 17

# User choice
guess = ""
choseHeads = True


# Simulate coin toss
def toss():
    global heads
    global tails
    global edges

    outcome = random.randrange(1, 100001, 1)
    if outcome <= edges:
        print('Wow the coin landed on its edge, try again')
    elif outcome <= heads + edges:
        if choseHeads:
            print("Lucky you, it's heads")
        else:
            print("Better luck next time, it's heads")
    elif outcome <= tails + edges + heads:
        if not choseHeads:
            print("YOU WIN, it's tails")
        else:
            print("Uh oh, it's tails")
    else:
        print("There was an error, try again")


# Get the user's choice
def getGuess():
    global guess
    global choseHeads

    guess = input("Heads or tails?\n").lower().strip()
    # Force the user to take tails if they give an invalid response
    if guess[0] == "h":
        choseHeads = True
        print("Tossing the coin, your choice is heads")
        toss()
    else:
        choseHeads = False
        print("Tossing the coin, your choice is tails")
        toss()


# Start the program
getGuess()
