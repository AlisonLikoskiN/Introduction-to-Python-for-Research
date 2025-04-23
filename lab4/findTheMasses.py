"""
PosENQ - UFSC
Introduction to python to research - ENQ410034
Alison Likoski Neves - 202405086
Lab 4: SymPy
"""
####################################################################################################################
"""
Problem 4 - Find the masses
Use SymPy to find the unknows in the following linear system:
0.9 m1 + 0.3 m2 + 0.1 m3 = 30
0.1 m1 + 0.5 m2 + 0.2 m3 = 25
0.2 m2 + 0.7 m3 = 30

Did you see any advantage in comparison of using a matrix within NumPy? Discuss it super briefly :)

"""
####################################################################################################################
# Libs
import sympy as sp

####################################################################################################################
# Functions
def draw(): # Just a function to make the terminal prettier =) (and faster to print LOL)
    print()
    print("___" * 30)
    print()

def massFinder():
    # Symbols
    m1, m2, m3 = sp.symbols("m1 m2 m3")
    
    # Equations
    eq1 = 0.9 * m1 + 0.3 * m2 + 0.1 * m3 - 30
    eq2 = 0.1 * m1 + 0.5 * m2 + 0.2 * m3 - 25
    eq3 = 0.2 * m2 + 0.7 * m3 - 30

    # Solving the system
    masses = sp.solve((eq1, eq2, eq3),(m1, m2, m3), dict=True)

    return masses

####################################################################################################################
draw()
print("Lab - Find the masses")
print("By: Alison Likoski Neves")
draw()

masses = massFinder()

print("Value of masses:")
print(f" {masses[0]}")
draw()

"""
Did you see any advantage in comparison of using a matrix within NumPy? Discuss it super briefly :)
Yes, with SymPy we just set the symbols, equations and solve it, and with NumPy matrix, takes more efforts and 
time to set things right (set coeff. matrix, then set the Y matrix and solve).
"""