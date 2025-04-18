# Lab 1 - Problem 1 - Magic Dungeon
# PosEnq UFSC
# Alison Likoski Neves

import random

possibleWays = ['foward', 'back', 'right', 'left'] # List with the possible ways to player

# Function to simulate the right way
def path():
    return random.choice(possibleWays) # Uses the random function to choice a random option of the possible ways

# Function to get the player's answer
def playerPath():
    playerChoice = input("Choose your way: ").lower() # Ask the direction and normalize to lower chars to avoid erros like "Back != back"
    
    # Check if the playerChoice really exist
    if playerChoice in possibleWays:
        return playerChoice
    else:
        print("Please, insert a valid option.") 
        return
    
# Main dungeon loop
dungeonRooms = 3 # Change with the number of rooms

for i in range (dungeonRooms):
    while True:
        print("You entered the room")

        rightPath = path() # Get a random right path by the function "path" (line 10)
        choice = playerPath() # Get the player answer by the function "playerPath" (line 14)

        # Check if the player answer is the right direction
        if choice == rightPath:
            print("Room exited!")
            print()
            break
        else:
            print("Wrong direction.")
            print()

# After all the rooms and exiting the dungeon, display the winning message.
print("You win!!")    

