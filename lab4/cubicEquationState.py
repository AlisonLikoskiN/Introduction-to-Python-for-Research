"""
PosENQ - UFSC
Introduction to python to research - ENQ410034
Alison Likoski Neves - 202405086
Lab 4: SymPy
"""
####################################################################################################################
"""
Problem 5 - Cubic Equation State

Perform the calculation to determine the specific volume of ammonia at a temperature (T) of 420K and a pressure (P)
of 43.4 atm, utilizing a cubic equation of state and using SymPy.

####################################################################################################################
The cubic equation of state choosen is the Peng-Robinson equation.
P = R * T / (Vm - b) - (a * alpha(T)) / (Vm **2 + 2 * b * Vm - b **2)

where:
a = 0.45724 * R **2 * Tc **2 / Pc
b = 0.07780 * R * Tc / Pc
alpha(T) = (1 + m * (1 - (T / Tc) ** 0.5)) ** 2
m = 0.37464 + 1.54226 * w - 0.26992 * w **2

for ammonia:
Tc = 405.5 K
Pc = 113.5 bar
w = 0.25

R = 0.08314 L * bar / (K * mol)
P = 43.4 atm --> 44 bar
"""
####################################################################################################################
# Libs
import sympy as sp

####################################################################################################################
# Constants
Tc = 405.5 # K
Pc = 113.5 # bar
w = 0.25 # Ammonia
R = 0.08314 # L * bar / (K * mol)
P = 44 # bar
T = 420 # K
M = 0.01703 # kg/mol (Molar mass of ammonia)
m = 0.37464 + 1.54226 * w - 0.26992 * w **2 # Ammonia
alphaT = (1 + m * (1 - (T / Tc) ** 0.5)) ** 2 # Ammonia
a = 0.45724 * R **2 * Tc **2 / Pc # Ammonia
b = 0.07780 * R * Tc / Pc # Ammonia

####################################################################################################################
# Functions
def draw(): # Just a function to make the terminal prettier =) (and faster to print LOL)
    print()
    print("___" * 30)
    print()

def robinsonPenguin():
    # Symbols
    Vm = sp.symbols("Vm")

    # Equation
    penguinDoRobinson = (R * T) / (Vm - b) - (a * alphaT) / (Vm **2 + 2 * b * Vm - b **2) - P

    # Solving the equation
    solved = sp.solve((penguinDoRobinson), (Vm), dict = True) # Dict = True > return as a dictionary

    return solved

####################################################################################################################
draw()
print("Lab - Quadratic formula")
print("By: Alison Likoski Neves")
draw()

specificVolume = robinsonPenguin()
print(f"There are {len(specificVolume)} different values of Vm (Molar Volume)")
print("The values are:")
for i in range(len(specificVolume)):
    print(f"Vm{i+1} = {specificVolume[i]}")
draw()
