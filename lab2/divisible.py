"""
PosENQ - UFSC
Introduction to python to research - ENQ410034
Alison Likoski Neves - 202405086
Lab 2: Booleans, Conditionals, and Loops
"""
####################################################################################################################
"""
Problem 1 - Divisible 2, 3?
Givem a number, the task is to check if a number is divisible by 2, 3, or not.
Write a program that asks for a number and afterward displays if it is divisible by 2, 3, or none.
"""
####################################################################################################################


# Asking the user for a number
print("Please, insert a number: ")
number = int(input()) # Converting the input number from string to integer

# Calculations and displays

if number%2 == 0 and number%3 == 0: # Check if the number is divisible by 2 AND 3
    print("The number is divisible by 2 and 3") # Displays results
elif number%2 == 0: # If not by 2 AND 3, the number is divisible by 2?
    print("The number is divisible by 2, not by 3") # Displays results
elif number%3 == 0: # If not by 2 AND 3, or by 2, is the number divisible by 3?
    print("The number is divisible by 3, not by 2") # Displays results
else: # If neither options, then the number is not divisible by 2 AND 3, or by 2 or by 3.
    print("The number is not divisible by 2 or 3") # Displays results
