"""
PosENQ - UFSC
Introduction to python to research - ENQ410034
Alison Likoski Neves - 202405086
Lab 4: SymPy
"""
####################################################################################################################
"""
Problem 1 - Quadratic formula
The quadratic formula is used to find the solutions (roots) of a quadratic equation, which is an equation of the form:
                    ax² + bx + c = 0
where a, b and c are coefficients, and x represents the variable we are trying to solve for. Use Sympy to find
the widely used quadratic formula.

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

def quadratic():
    # Symbols
    a, b, c, x = sp.symbols("a b c x")

    # Equation
    qdF = a * x**2 + b * x + c

    # Solving the equation
    solved = sp.solve((qdF), (x), dict = True) # Dict = True > return as a dictionary

    return solved

####################################################################################################################
draw()
print("Lab - Quadratic formula")
print("By: Alison Likoski Neves")
draw()

answer = quadratic()
print(f"X1 = {answer[0]}")
print(f"X2 = {answer[1]}")
draw()