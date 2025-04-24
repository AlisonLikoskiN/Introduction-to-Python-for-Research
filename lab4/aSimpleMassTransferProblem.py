"""
PosENQ - UFSC
Introduction to python to research - ENQ410034
Alison Likoski Neves - 202405086
Lab 4: SymPy
"""
####################################################################################################################
"""
Problem 3 - A simple mass transfer problem
Consider a one-dimensional steady-state mass transfer problem in a slab with a constant diffusion coeeficient D. 
The concentration of a solute C in the slab satisfies the following differential equation:

                    d²C/dx² = 0 

    where x is the spatial coordinate along the slab.
    Boundary conditions: The following boundary conditions are given:

    C(x=0) = C0 # Concentration at x = 0
    C(x=L) = CL # Concentration at x = L

    Where C0 and CL are know constants representing the concentration at the two ends of the slab, and L is the length
    of the slab. Use SymPy to solve this differential equation and determine the concentration profile C(x) in the slab.
"""
####################################################################################################################
# Libs
import sympy as sp

####################################################################################################################
# Constants 



####################################################################################################################
# Functions
def draw(): # Just a function to make the terminal prettier =) (and faster to print LOL)
    print()
    print("___" * 30)
    print()

def massFinder():
    # Symbols
    x, L, C0, CL = sp.symbols('x L C0 CL')  
    C = sp.Function('C')(x) # Concentration as a function of x

    # Rate equation
    eq = C.diff(x, x) # Second derivative of C with respect to x


    # Solving the system
    solution = sp.diff(eq, x)  # Differentiate the equation

    # Boundary conditions
    ics = { C.subs(x,0): C0, C.diff().subs(x, L): CL}

    # Solving the differential equation using the boundary conditions
    solution = sp.dsolve(eq, ics=ics)

    print(solution)

    # Taking the solution values



    return 

####################################################################################################################
# Intro
draw()
print("Lab - A Simple mass transfer problem")
print("By: Alison Likoski Neves")
draw()

# Solving the system

print("The solution of the system is:")

massFinder()

draw()





