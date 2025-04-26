"""
PosENQ - UFSC
Introduction to python to research - ENQ410034
Alison Likoski Neves - 202405086
Lab 5: thermo 
"""
####################################################################################################################
"""
Problem 2 - Thermodynamic volumes 

Given that the vapor pressure for n-butane at 350 K is 9.4573 bar, find the molar volumes of a) saturated vapor and 
b) saturated liquid of n-butane at these conditions using the following equations of state using Thermo: 
Van der Waals, Redlich-Kwong, Soave- Redlich-Kwong, and Peng-Robinson. 
Compare with the experimental values (Vv = 2482 cm3/mol  Vl =115.0 cm3/mol) 

"""
####################################################################################################################
# Libs
from thermo.chemical import Chemical
from thermo.eos import VDW, PR, RK, SRK

####################################################################################################################
# Constants

temperature = 350 # K
pressure = 945730 # Pa
expVapor = 2482   # cm3/mol
expLiquid = 115.0 # cm3/mol

####################################################################################################################
# Functions
def draw(): # Just a function to make the terminal prettier =) (and faster to print LOL)
    print()
    print("___" * 30)
    print()
####################################################################################################################
draw()
print("Lab - Thermodynamic volumes")
print("By: Alison Likoski Neves")
draw()

# Choosing the substance and storage in a variable
nbutane = Chemical('n-butane', T=temperature, P=pressure)
"""
Taking the substance properties into a variable.
When using google colab, this step is not necessary, since we can call the function and use "substance.property".
But as commented in the class by the professor, in some cases (or editors) it is not possible to do this.
And this way its easier to read and its also a good practice.
"""
Tc = nbutane.Tc # Critical temperature 
Pc = nbutane.Pc # Critical pressure
omega = nbutane.omega

# Taking the values of molar volume to (a) saturated vapor and (b) saturated liquid
# Answer in a array of: array[vapor, liquid]

# Van der Waals > VDW(Tc, Pc, T = None, P = None, V = None, omega = None)
vanDerWaals = [(VDW(Tc = Tc, Pc = Pc, T = temperature, P = pressure).V_g) , (VDW(Tc = Tc, Pc = Pc, T = temperature, P = pressure).V_l)]

# Redlich-Kwong > RK(Tc, Pc, T = None, P = None, V = None, Omega = None)
redlichKwong = [RK(Tc = Tc, Pc = Pc, T = temperature, P = pressure).V_g, RK(Tc = Tc, Pc = Pc, T = temperature, P = pressure).V_l]

# Soave-Redlich-Kwong > RDK(Tc, Pc, omega, T = None, P = None, V = None)
soaveRedlichKwong = [SRK(Tc = Tc, Pc = Pc, omega = omega, T = temperature, P = pressure).V_g, SRK(Tc = Tc, Pc = Pc, omega = omega, T = temperature, P = pressure).V_l]

# Peng-Robinson > PR(Tc, Pc, omega, T = None, P = None, V = None)
pingwinRobinson = [PR(Tc = Tc, Pc = Pc, omega = omega, T = temperature, P = pressure).V_g , PR(Tc = Tc, Pc = Pc, omega = omega, T = temperature, P = pressure).V_l]

# Its needed to convert the values from m³/mol to cm³/mol (1 m³ = 1000000 cm³)
convert = 1000000

for i in range(2):
    vanDerWaals[i] = vanDerWaals[i] * convert
    redlichKwong[i] = redlichKwong[i] * convert
    soaveRedlichKwong[i] = soaveRedlichKwong[i] * convert
    pingwinRobinson[i] = pingwinRobinson[i] * convert

# Printing the results
print("The values of the molar volume are:")
print(f"Van der Waals: {vanDerWaals[0]} cm³/mol (vapor) and {vanDerWaals[1]} cm³/mol (liquid)")
print(f"Redlich-Kwong: {redlichKwong[0]} cm³/mol (vapor) and {redlichKwong[1]} cm³/mol (liquid)")
print(f"Soave-Redlich-Kwong: {soaveRedlichKwong[0]} cm³/mol (vapor) and {soaveRedlichKwong[1]} cm³/mol (liquid)")
print(f"Peng-Robinson: {pingwinRobinson[0]} cm³/mol (vapor) and {pingwinRobinson[1]} cm³/mol (liquid)")
print(f"Experimental values: {expVapor} cm³/mol (vapor) and {expLiquid} cm³/mol (liquid)")
draw()





