"""
PosENQ - UFSC
Introduction to python to research - ENQ410034
Alison Likoski Neves - 202405086
Lab 5: thermo 
"""
####################################################################################################################
"""
Problem 5 - Steam tables

Verify if the embedded calculations within Thermo are reliable for water, 
and check pressure and temperature dependencies using steam tables to compare. 

"""
####################################################################################################################
# Libs
from thermo.chemical import Chemical
import numpy as np


####################################################################################################################
# Constants

temperatures = np.linspace(10, 100, 10)
pressures = [1.227, 2.339, 4.246, 7.384, 12.350, 19.941, 31.19, 47.39, 70.14, 101.3] # KPa
CpTable = [41.99, 83.94, 125.77, 167.53, 209.30, 251.09, 292.93, 334.84, 376.82, 418.91]
RhoLiqTable = [999.69, 998.19, 995.61, 992.17, 987.99, 983.16, 977.75, 971.79, 965.33, 954.75]

for i in range(len(pressures)):
    pressures[i] = pressures[i] * 1000 # Convert to Pa
####################################################################################################################
# Functions
def draw(): # Just a function to make the terminal prettier =) (and faster to print LOL)
    print()
    print("___" * 30)
    print()
####################################################################################################################
draw()
print("Lab - Steam Tables")
print("By: Alison Likoski Neves")
draw()

# Printing the values of Cp(T,P) from tables vs Thermo values
print("Cp(T,P) from tables vs Thermo values")
print("___"*30)
print("T(C)   | P(Pa)       | Cp(T,P) from tables  | Cp(T,P) from Thermo")
print("___"*30)
for i in range(len(temperatures)):
    CpWater = Chemical("Water", T=temperatures[i], P=pressures[i]).Cp
    print(f"{temperatures[i]}   | {pressures[i]}      | {CpTable[i]}               | {CpWater}")
print("___"*30)

# Printing the values of RhoLiquid(T,P) from tables vs Thermo values
print("RhoLiquid(T,P) from tables vs Thermo values")
print("___"*30)
print("T(C)   | P(Pa)       | RhoLiquid(T,P) from tables  | RhoLiquid(T,P) from Thermo")
print("___"*30)
for i in range(len(temperatures)):
    RhoWater = Chemical("Water", T=temperatures[i], P=pressures[i]).rhol
    print(f"{temperatures[i]}   | {pressures[i]}      | {RhoLiqTable[i]}               | {RhoWater}")
print("___"*30)

"""
Is possible to see that the values of thermos and the official tables are close, but there's a difference.
This difference need to be analysed and take in consideration depending of the application.
"""


