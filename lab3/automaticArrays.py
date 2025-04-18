"""
PosENQ - UFSC
Introduction to python to research - ENQ410034
Alison Likoski Neves - 202405086
Lab 3: NumPy and SciPy
"""
####################################################################################################################
"""
Problem 5 - Automatic arrays

Generate the following vectors within a script using > linspace() < and > arange() < printing them on the shell:
[0 1 2 3 4 5 6 7 8 9 10]
[1 2 3 4 5 6 7 8 9]
[1 2 3 4 5 6 7 8 9 10]
[0 1 2 3 4 5 6 7 8 9]
Use the first arrays as >x<, generate the vector >w< (below), using x assigning 33 to the 3rd position as:
[0 1 33 3 4 5 6 7 8 9 10]
Use x and w, and find y = x**3
[0 1 8 27 64 125 216 343 512 729 1000]
and z = w**3
[0 1 35937 27 64 125 216 343 512 729 1000]
"""
####################################################################################################################
# Libs
import numpy as np

####################################################################################################################
# Functions
def draw(): # Just a function to make the terminal prettier =) (and faster to print LOL)
    print()
    print("___" * 30)
    print()

####################################################################################################################
print("Lab 3 - Automatic arrays")
draw()

# Generating the vectors with arange(start, stop(not included), step) and linspace(start, stop(included), n)

# arange()

ar1 = np.arange(0, 11, 1)
ar2 = np.arange(1, 10, 1)
ar3 = np.arange(1, 11, 1)
ar4 = np.arange(0, 10, 1)

print("Vectors created using arange()")
print(ar1)
print(ar2)
print(ar3)
print(ar4)
draw()

# linspace
ls1 = np.linspace(0, 10, 11)
ls2 = np.linspace(1, 9, 9)
ls3 = np.linspace(1, 10, 10)
ls4 = np.linspace(0, 9, 10)

print("Vectors created using linspace()")
print(ls1)
print(ls2)
print(ls3)
print(ls4)
draw()

# Copy the first array as x
x = np.copy(ls1)
print("Array x = ", x)
# Creating vector w and changing w[2] = 33
w = np.linspace(0, 10, 11)
w[2] = 33
print("Vector w = ", w)
draw()

# Creating y = x³ and z = w³
# it's possible to create like
y = x**3
#and
z = w**3

print("Array y = ", y)
print("Array z =", z)
# But this way we have a alias problem
draw()

# To avoid aliasing, we can use np.copy()
y2 = np.copy(x**3)
z2 = np.copy(w**3)

print("New array y = ", y2)
print("New array z = ", z2)
draw()


