"""
PosENQ - UFSC
Introduction to python to research - ENQ410034
Alison Likoski Neves - 202405086
Lab 3: NumPy and SciPy
"""
####################################################################################################################
"""
Problem 4 - Find the masses
Use SciPy to find the unknows in the following linear system:
0.9 m1 + 0.3 m2 + 0.1 m3 = 30
0.1 m1 + 0.5 m2 + 0.2 m3 = 25
0.2 m2 + 0.7 m3 = 30

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
print("Lab 4 - Find the masses")
draw()

# Creating arrays > array[vector(m1, m2, m3), vector(m1, m2, m3), vector(m1, m2, m3)]

values = np.array([[0.9, 0.3, 0.1],[0.1, 0.5, 0.2],[0, 0.2, 0.7]])
print("Values matrix = ")
print(values)

draw()

y = np.array([30, 25, 30])
print("y matrix = ")
print(y)

draw()

masses = nl.solve(values, y)

print("The masses values are = ")
print(f"m1 = {masses[0]}")
print(f"m2 = {masses[1]}")
print(f"m3 = {masses[2]}")

draw()