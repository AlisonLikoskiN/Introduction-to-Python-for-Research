"""
PosENQ - UFSC
Introduction to python to research - ENQ410034
Alison Likoski Neves - 202405086
Lab 3: NumPy and SciPy
"""
####################################################################################################################
"""
Problem 3 - Derive x³
Write a code that finds the numerical derivative of y in problem 1 using 2 different approaches:
1) Forward differences
2) Central differences

Where i is the array position.

Refine the derivative increasing the array size for the same interval[0,10], note that n in problem 1 is 11. Use n equal to 101 and 1001.
Conclude the observation of n and the approximation.

"""
####################################################################################################################
# Libs
import numpy as np
import numpy.linalg as nl

####################################################################################################################
# Functions
def draw(): # Just a function to make the terminal prettier =) (and faster to print LOL)
    print()
    print("___" * 30)
    print()


####################################################################################################################
print("Lab 3 - Derive x³")
draw()

# Main loop - Creating arrays and derivating for n = [11, 101, 1001]

n = [11, 101, 1001]

for j in n:
    print(f"Calculating for n = {j}")

    # Creating x and y
    x = np.linspace(0, 10, j)
    y = np.copy(x**3)

    print("Array x = ")
    print(x)
    draw()

    # Derivating
    
    
    dydxForward = np.ones(j-1)
    for i in range(j-1):
            dydxForward[i] = (y[i+1] - y[i]) / (x[i+1] - x[i])

    dydxCentral = np.ones(j-1)
    for i in range(1, j-1):
        dydxCentral[i-1] = (y[i+1] - y[i-1]) / (x[i+1] - x[i-1])

    # This way we dont have the matrixes with the same lenght, but i forgot to do this earlier and dont have more time to improve =(

    print("Forward Differences = ")
    print(dydxForward)

    print("Central Differences = ")
    print(dydxCentral)

    # Real Derivative

    print("Real Derivative = ")
    print(3 * x**2)
    draw()

    """
    When you increase the array size (n = 11 > 101 > 1001) the precision of dydx (forward and central) gets closer to the real derivative.
    Due to the way arrays works, the calculated differences arrays, will be smaller than the real derivative array.
    If we have a array > array(n)
    We cant access array(n+1) and array(0-1) in the for loop, and when we try it, we receive a error
    So, to avoid this, is necessary do more conditionals, changing especific values in the equation (to n+1 and 0-1)
    """






