"""
PosENQ - UFSC
Introduction to python to research - ENQ410034
Alison Likoski Neves - 202405086
Lab 2: Booleans, Conditionals, and Loops
"""
####################################################################################################################
"""
Problem 2 - Heron`s Method
Heron's method is an algorithm for approximating the square root of a non-negative real number. 
It is named after the Greek mathematician Heron of Alexandria. 
The method involves starting with an initial guess for the square root and then iteratively improving the guess until it converges to the actual value. 
The basic steps of Heron's method are as follows: 
- 1. Start with an initial guess for the square root of the given number. 
- 2. Compute the average of the guess and the given number divided by the guess. 
- 3. Use the result from step 2 as the new guess. 
- 4. Repeat steps 2 and 3 until the guess converges to the actual square root. 
"""
####################################################################################################################

# Import libs

import math # Lib math to check the real answer
####################################################################################################################
# Functions

# Function to calculate the guess number
def heronsMtd(number, guess): # Inputs: user number and the guess number
    """
    Calculates the herons method.
    Number: Number from the user
    Guess: Guess number to use in Heron`s Method.
    New Guess = [Guess + (number / guess)] / 2
    """
    newGuess = (guess + (number / guess)) / 2
    return newGuess

####################################################################################################################


print("Heron`s Method Calculator")

# Number input by user
numberUser = -1 
while numberUser < 0: # Just to make sure the number is positive =)
    print("Please, insert a positive number: ")
    numberUser = float(input())

rootHerons = numberUser / 2  # Initial guess value
realRoot = math.sqrt(numberUser) # Real sqrt root of the number, used to compare the results
error = 1e-4 # Acceptable error between the realRoot and rootHerons
i = 0 # Variable just to know how many iterations was made (bc I`m curious)

while abs(rootHerons - realRoot) > error: # While the absolute value of the diference between both number is greater than the error, do:
    rootHerons = heronsMtd(numberUser, rootHerons) # Use the function "heronsMtd" to get a new guess
    i +=1 

# Display the answer
print("____"*10)
print(f"Calculation completed after {i} iterations.")
print(f"The calculated square root of {numberUser} is {rootHerons}")
print(f"The real value of the square root is {realRoot}")
print("____"*10)

