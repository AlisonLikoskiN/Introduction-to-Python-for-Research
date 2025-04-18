"""
PosENQ - UFSC
Introduction to python to research - ENQ410034
Alison Likoski Neves - 202405086
Lab 2: Booleans, Conditionals, and Loops
"""
####################################################################################################################
"""
Problem 5 - Gaming up to you! - Hangman
Hangman is a well know game where you have a secret word. 
The player needs to guess the word suggesting letter by letter. 
If the player`s guess is wrong, a draw of a hanged man is made, part by part.
The game ends when you guess the word or the draw is full.
"""

"""
___________
|  /       O
| /       /|\
|/         /\
|

6 Parts to be draw (head, arms, body and legs) = 6 lifes
"""
####################################################################################################################

# Functions

def draw(lifes): # Draw the hangman in terminal =)
    if lifes == 6:
        lifes6()
    if lifes == 5:
        lifes5()
    if lifes == 4:
        lifes4()
    if lifes == 3:
        lifes3()
    if lifes == 2:
        lifes2()
    if lifes == 1:
        lifes1()
    if lifes == 0:
        lifes0()
    return

# Getting the char from player
def getChar():
    while True: # Loop to make sure it insert only one letter
        char = input()
        if len(char) == 1 and char.isalpha(): # If it`s only a character and this character is a alpha letter, do:
            return char
        else: # If not, ask again
            print("Please, insert only one letter.")

def checkChar(char,lifes):
    # Check if the letter is in the word
    # If is, reveal the letter
    # If not, -1 life
    if char in word: 
        print("You made the right guess! =)")
    else:
        print("You made the wrong guess! =(")
        lifes -=1

    # Change the # of secret to the char (only if char is in the word)
    for c in range(len(word)): # Iterates for each letter in word
        if char == word[c]: # Checks if char is equals to the letter in word
            secret[c] = char # Changes 

    return lifes   # Return the remaining lifes


def lifes6():
    print("___________")
    print("|  /")
    print("| / ")
    print("|/ ")
    print("|")
    print()
    return

def lifes5():
    print("___________")
    print("|  /       O")
    print("| / ")
    print("|/ ")
    print("|")
    print()
    return

def lifes4():
    print("___________")
    print("|  /       O")
    print("| /       /")
    print("|/ ")
    print("|")
    print()
    return
        
def lifes3():
    print("___________")
    print("|  /       O")
    print("| /       /|")
    print("|/ ")
    print("|")
    print()
    return

def lifes2():
    print("___________")
    print("|  /       O")
    print("| /       /|\ ")
    print("|/ ")
    print("|")
    print()
    return

def lifes1():
    print("___________")
    print("|  /       O")
    print("| /       /|\ ")
    print("|/         /")
    print("|")
    print()
    return

def lifes0():
    print("___________")
    print("|  /       O")
    print("| /       /|\ ")
    print("|/         /\ ")
    print("|")
    print()
    return
####################################################################################################################

# Welcome
lifes = 6 # Initial lifes
print("____"*10)
print("Welcome to the hangman game!")
draw(lifes)
print("____"*10)

# Getting the secret word
print("Please, insert the secret word: ")
while True: # Loop to make sure the word is a alpha character word, not simbols or numbers
    word = input().lower() # Get the word
    if word.isalpha(): # Check the condition 
        break
    else:
        print("A word, not number or other characters...")

# Creating a list of ##### to display the secret word
secret = list(word) # Transform a word into a list of letters
for i in range(len(secret)): # Iterate for each letter in the size of the list
    secret[i] = "#" # Changes the letter to "#"


# Main game loop
while True:
    # Get a character
    # Check if the char is in the word
    # if
        # Char is in word
            # Reveals the word
        # Char is not in word
            # Loses 1 life
    # Endgame when
        # Loses all lifes
        # Guess the full word

    print("The word is: ")
    print(secret)

    # Get the letter from user

    print("____"*10)
    print("Please, insert a letter: ")
    char = getChar().lower() # Using only lower letter to avoid problems with "a != A"

    # Check if the char in in the word
    lifes = checkChar(char, lifes) 
    draw(lifes) # Draw the hangman
    print("____"*10)

    # Endgame Conditionals
    if lifes == 0: # Game over, lifes = 0
        print("You did not guessed the word =(")
        print("Game over!")
        break

    if secret == list(word): # Winning, list of letters in secret = list of letters in word
        print("You guessed the word! =)")
        print("You win!")
        break
