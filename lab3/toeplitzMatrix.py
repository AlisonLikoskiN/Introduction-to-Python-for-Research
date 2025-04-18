"""
PosENQ - UFSC
Introduction to python to research - ENQ410034
Alison Likoski Neves - 202405086
Lab 3: NumPy and SciPy
"""
####################################################################################################################
"""
Problem 2 - Toeplitz Matrix
Write a script that generates a square tridiagonal Toeplitz-type Matrix of shape (n,n), where n is an integer
typed bu the code user. The Toeplitz matrix is characterized by the main diagonal being two and the diagonals next 
to the principal being -1 for any n.

For example, for n = 3:
[ 2 -1  0]
[-1  2 -1]
[ 0 -1  2]

Generate 3 vectors, one constant, another with linear growth, and another with quadratic growth, and multiply the 
matrix with those vectors. Ignoring the first and last row can you conclude something?

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

def getNum(): # Functino to get a (positive) integer number from user
    print("Please, insert a integer number:")
    num = -1
    while True:
        num = int(input())
        if num > 0:
            return num
        else:
            print("A >> Positive << number!")


####################################################################################################################
print("Lab 3 - Toeplitz Matrix")
draw()

# Getting user number and creating the matrix
n = getNum()
draw()

# Creating a empty matrix first
tpMtx = np.zeros((n,n))

# Making the empty array into the toeplitz matrix
tpMtx[0,0] = 2 # First n# 2
tpMtx[-1, -1] = 2 # Last n# 2
tpMtx[0, 1] = -1
tpMtx[-1, -2] = -1

for i in range(1, n-1):
    tpMtx[i,i] = 2
    tpMtx[i,i+1] = -1
    tpMtx[i,i-1] = -1

print("The Toeplitz Matrix created is: ")
print(tpMtx)
draw()
"""
When you ignore the first and last row (because with a array(n,n) you can`t access array(n+1,n+1) or array(0-1, 0-1)).
The rest of the toeplitz matrix can be made by following a for loop, where:
array(i,i) are the diagonals (number = 2)
array(i,i+1) are the diagonal plus 1 (number = -1)
array(i,i-1) are the diagonal minus 1 (number = -1)
"""

# Creating the 3 vectors: constant, linear, quadratic

# Constant
cteVector = np.ones(n) * 3
print("Constant vector is: ")
print(cteVector)

# Linear 
lnrVector = np.arange(0, n, 1)
print("Linear vector is: ")
print(lnrVector)
# Quadratic 
qdtVector = np.arange(0, n, 1) ** 2
print("Quadratic vector is: ")
print(qdtVector)

draw()

# Multipling the matrix by the vector

toepCte = nl.solve(tpMtx, cteVector)
toepLnr = nl.solve(tpMtx, lnrVector)
toepQdt = nl.solve(tpMtx, qdtVector)

print("Toeplitz x Constant")
print(toepCte)
print("Toeplitz x Linear")
print(toepLnr)
print("Toeplitz x Quadratic")
print(toepQdt)

draw()

