"""
PosENQ - UFSC
Introduction to python to research - ENQ410034
Alison Likoski Neves - 202405086
Lab 5: Thermo
"""
####################################################################################################################
"""
Problem 4 - SymPy vs Thermo

Do you remember problem 5 from the SymPy lab? 
Perform the calculation to determine the specific volume of ammonia at a temperature (T) of 420 K 
and a pressure (P) of 43.4 atm, utilizing the same cubic equation of state using SymPy and Thermo to compare.  

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
from thermo.chemical import Chemical
from thermo.eos import PR

####################################################################################################################
#                                  SymPy CALCULATION                                                               #
####################################################################################################################
# Constants used to SymPy Calculation
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

def robinsonPingwin():
    # Symbols
    Vm = sp.symbols("Vm")

    # Equation
    pingwinDoRobinson = (R * T) / (Vm - b) - (a * alphaT) / (Vm **2 + 2 * b * Vm - b **2) - P

    # Solving the equation
    solved = sp.solve((pingwinDoRobinson), (Vm), dict = True) # Dict = True > return as a dictionary

    return solved

####################################################################################################################
draw()
print("Lab - SymPy vs Thermo")
print("By: Alison Likoski Neves")
draw()

print("SymPy calculation")
specificVolume = robinsonPingwin()
print(f"There are {len(specificVolume)} different values of Vm (Molar Volume)")
print("The values are:")
for i in range(len(specificVolume)):
    print(f"Vm{i+1} = {specificVolume[i]} ")
print(f"Value really used: Vm = {specificVolume[0]} L/mol")
draw()

####################################################################################################################
#                                  Thermo CALCULATION                                                              #
####################################################################################################################
tThermo = 420
pThermo = 43.4 * 100000
convert = 1000 # m³ to L
# Instance of the chemical substance
demonia = Chemical("ammonia", T = tThermo, P = pThermo)
TcThermo = demonia.Tc
PcThermo = demonia.Pc
omegaThermo = demonia.omega

# Calculation using Peng-Robinson equation from thermo lib
pengRobinson = (PR(Tc = TcThermo, Pc = PcThermo, omega = omegaThermo, T = tThermo, P = pThermo).V_g) * convert
print(f"Value from thermo lib is: {pengRobinson} L/mol")
draw()




