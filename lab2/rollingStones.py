"""
PosENQ - UFSC
Introduction to python to research - ENQ410034
Alison Likoski Neves - 202405086
Lab 2: Booleans, Conditionals, and Loops
"""
####################################################################################################################
"""
Problem 3 - Rolling Stones
Write a program to play this game!
The game consist of two players sitting before a pile of stones.
The users define the number of stones.
The players take turns, each removing between 1 and 5 stones.
The person who draws the last rock wins.
"""
####################################################################################################################

# Functions

# Getting a number of rocks/stones to remove between 1 and 5
def gettingStones():
    stones = 0
    while stones < 1 or stones > 5:
        stones = int(input())
        if stones < 1 or stones > 5:
            print("Please, insert a valid value between 1 and 5 stones")
        else:
            return stones


####################################################################################################################


# Welcome
print("____"*10)
print("Welcome to the Rolling Stones game!")
print("____"*10)

# Player names
print("Please, insert the name of the players")
player1 = input("Player 1: ")
player2 = input("Player 2: ")
print("____"*10)

# Getting the number of rocks from user
print("Please, insert the number of stones")
rocks = -1
while rocks < 1: # Loop to make sure it`s a positive number
    rocks = int(input())
    if rocks < 1:
        print("You need to insert a positive integer number of stones. Please, insert a new value.")

# Main game loop
remainingRocks = rocks
i = 0 # Just to count how much rounds was played

while remainingRocks > 0: # While still have rocks left, do the game:
    i +=1
    print("____"*10)
    print(f"Round {i}.")
    # Player 1
    print(f"{player1}, please insert the number of stones to remove:")
    stones = gettingStones()
    remainingRocks = remainingRocks - stones
    print(f"{stones} stone(s) was removed from the pile.")
    if remainingRocks < 1:
        print('All stones removed')
        print(f"Congratulations {player1}, you win!!")
        break
    print(f"{remainingRocks} stones remaining.")

    # Player 2
    print(f"{player2}, please insert the number of stones to remove:")
    stones = gettingStones()
    remainingRocks = remainingRocks - stones
    print(f"{stones} stone(s) was removed from the pile.")
    if remainingRocks < 1:
        print('All stones removed')
        print(f"Congratulations {player2}, you win!!")
        break
    print(f"{remainingRocks} stones remaining.")
