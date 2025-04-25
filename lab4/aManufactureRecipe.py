"""
PosENQ - UFSC
Introduction to python to research - ENQ410034
Alison Likoski Neves - 202405086
Lab 4: SymPy
"""
####################################################################################################################
"""
Problem 4 - A manufacture recipe
A manufacture is engaged in the production of a formulation S containing ingredients A, B, C and D, containing 
25 lbm of each. For this requieres the blending of three formulations, namely M1, M2 and M3, to achieve the desired
product. The manufacturer needs to determine the fractions of B and D in M2 named xb and xd, respectively. 
The manufacturer also needs to determine the rates at wich the formulations M1, M2 and M3 must enter the process.
To solve this problem, a set of equations can be structured using material balances to determine the unknown variables,
see the flowsheet of the process below for more details.

                        M1
                        A 60% wt
                        B 20% wt
                        C 20% wt
                        ###########
            M2          #         # S
            A 20% wt    #  MIXER  # A 25 lbm
            B xb        #         # B 25 lbm
            D xd        #         # C 25 lbm
                        #         # D 25 lbm
                        ###########
                        M3
                        A 20% wt
                        C 60% wt
                        D 20% wt
Estabilish the equations for the following problem and solve it using SymPy. 
Did you see any advantage in comparison of using a matrix within NumPy? Discuss it super briefly :)            
"""
####################################################################################################################
# Libs
import sympy as sp

####################################################################################################################
# Constants 
# array[M1, M2, M3]
A = [0.6, 0.2, 0.2] # wt% of A in M1, M2 and M3
B = [0.2, 0, 0] # wt% of B in M1, M2 and M3
C = [0.2, 0, 0.6]
D = [0, 0, 0.2] # wt% of D in M1 and M3
S = [25, 25, 25, 25] # lbm of A, B, C and D in S


####################################################################################################################
# Functions
def draw(): # Just a function to make the terminal prettier =) (and faster to print LOL)
    print()
    print("___" * 30)
    print()

def massFinder():
    # Symbols
    m1, m2, m3, xb, xd = sp.symbols("m1 m2 m3 xb xd")
    
    # Equations
    eq1 = m1 + m2 + m3 - (S[0] + S[1] + S[2] + S[3])    # Mass balance
    eq2 = A[0] * m1 + A[1] * m2 + A[2] * m3 - S[0]      # Mass balance of A
    eq3 = B[0] * m1 + xb *   m2 + B[2] * m3 - S[1]                    # Mass balance of B
    eq4 = C[0] * m1 + C[1] * m2 + C[2] * m3 - S[2]      # Mass balance of C  
    eq5 = D[0] * m1 + xd *   m2 + D[2] * m3 - S[3]        # Mass balance of D

    # Solving the system
    masses = sp.solve((eq1, eq2, eq3, eq4, eq5),(m1, m2, m3, xb, xd), dict=True)

    # Taking the solution values
    m1 = masses[0][m1]
    m2 = masses[0][m2]  
    m3 = masses[0][m3]
    xb = masses[0][xb]
    xd = masses[0][xd]


    return (m1, m2, m3, xb, xd)

####################################################################################################################
# Intro
draw()
print("Lab - A manufacture recipe")
print("By: Alison Likoski Neves")
draw()

# Solving the system
solution = massFinder()

# Printing the results

#       Masses
print("Value of masses:")   
print(f" M1 = {solution[0]} lbm")
print(f" M2 = {solution[1]} lbm")
print(f" M3 = {solution[2]} lbm")
draw()
#       Fractions
print("Value of fractions:")
print(f" xb = {solution[3]} % wt")
print(f" xd = {solution[4]} % wt")
draw()

#      Arrays
print("Array of fractions:")
B[1] = solution[3]
D[1] = solution[4]
print(f" A = {A} %wt")
print(f" B = {B} %wt")
print(f" C = {C} %wt")
print(f" D = {D} %wt")
draw()

"""
Did you see any advantage in comparison of using a matrix within NumPy? Discuss it super briefly :)

################################################################################################
 
Yes, with SymPy we just set the symbols, equations and solve it, and with NumPy matrix, takes more efforts and
time to set things right (set coeff. matrix, then set the Y matrix and solve).
In this case, a matrix would make it harder to understand and easier to make mistakes, and with numpy it probably would not work
because of the part "xb * m2" and "xd * m2", since its two variable in the same term, and with a matrix it would be not possible to solve it.
"""


