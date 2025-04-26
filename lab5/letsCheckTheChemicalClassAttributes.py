"""
PosENQ - UFSC
Introduction to python to research - ENQ410034
Alison Likoski Neves - 202405086
Lab 5: thermo 
"""
####################################################################################################################
"""
Problem 1 -  Let's check the Chemical class Attributes! 

Choose two different substances and calculate three different properties using the Chemical class within thermo. 
Check the values displayed compared with available thermodynamical data.  

####################################################################################################################

Substances choosen:
- Ethanol
- Water
- Ammonia

Substances properties:
- Molar mass
- Critical temperature
- Critical pressure

Properties of the substances choosen:
- Ethanol:
    - Molar mass: 46.068 g/mol
    - Critical temperature: 514.0 K
    - Critical pressure: 61.65 atm <> 6246686.3 Pa

- Water:
    - Molar mass: 18.015 g/mol
    - Critical temperature: 647.1 K
    - Critical pressure: 220.55 atm <> 22347228.8 Pa

- Ammonia:
    - Molar mass: 17.031 g/mol
    - Critical temperature: 405.5 K
    - Critical pressure: 113.5 atm <> 11500388 Pa

"""
####################################################################################################################
# Libs
from thermo.chemical import Chemical

####################################################################################################################
# Constants

# Table values
tabEthanol = [46.068, 514.0, 6246686] # g/mol, K, Pa
tabWater = [18.015, 647.1, 22347228] # g/mol, K, Pa
tabAmmonia = [17.031, 405.5, 11500388] # g/mol, K, Pa

####################################################################################################################
# Functions
def draw(): # Just a function to make the terminal prettier =) (and faster to print LOL)
    print()
    print("___" * 30)
    print()


####################################################################################################################
draw()
print("Lab - Let's check the Chemical class Attributes!")	
print("By: Alison Likoski Neves")
draw()

# Thermo lib chemical substances
thermoEthanol = Chemical("ethanol")
thermoWater = Chemical("water")
thermoAmmonia = Chemical("ammonia")

print("The substances are:")
print(thermoWater)
print(thermoEthanol)
print(thermoAmmonia)
draw()

# Thermo substances properties
thermEt = [thermoEthanol.MW, thermoEthanol.Tc, thermoEthanol.Pc]
thermWa = [thermoWater.MW, thermoWater.Tc, thermoWater.Pc]
thermAm = [thermoAmmonia.MW, thermoAmmonia.Tc, thermoAmmonia.Pc]

print("The properties of the substances from thermo lib are:")
print(f"Ethanol: {thermEt}")
print(f"Water: {thermWa}")
print(f"Ammonia: {thermAm}")
draw()

print("The properties of the substances from the table are:")
print(f"Ethanol: {tabEthanol}")
print(f"Water: {tabWater}")
print(f"Ammonia: {tabAmmonia}")
draw()

# Difference between the values:
difEthanol = [abs(thermEt[0] - tabEthanol[0]), abs(thermEt[1] - tabEthanol[1]), abs(thermEt[2] - tabEthanol[2])]
difWater = [abs(thermWa[0] - tabWater[0]), abs(thermWa[1] - tabWater[1]), abs(thermWa[2] - tabWater[2])]
difAmmonia = [abs(thermAm[0] - tabAmmonia[0]), abs(thermAm[1] - tabAmmonia[1]), abs(thermAm[2] - tabAmmonia[2])]

print("The difference between the values from the table and the values from the thermo lib are:")
print(f"Ethanol: {difEthanol}")
print(f"Water: {difWater}")
print(f"Ammonia: {difAmmonia}")
draw()

