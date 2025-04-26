"""
PosENQ - UFSC
Introduction to python to research - ENQ410034
Alison Likoski Neves - 202405086
Lab 5: thermo 
"""
####################################################################################################################
"""
Problem 3 - Booze?
Choose your preferred drink (if you don't like any, choose one for learning! :) ). 
Estimate at least five properties at room temperature and after being in your freezer for a while. 

####################################################################################################################

Drink chosen: Caipirinha
Caipirinha is a Brazilian cocktail made with cachaça (a sugarcane liquor), lemon, and sugar.
It is a refreshing drink that is popular in Brazil and around the world.
It is typically served over ice and is known for its sweet and tangy flavor.
It is a popular drink in Brazil and is often enjoyed during hot weather or at parties and celebrations.

####################################################################################################################

Recipe for this lab:
- lemon > is a bit difficult to represent with a python code, so I will not use it in this lab.
- water > I will use it to represent the ice and to substitute the lemon juice.
- cachaça > I will use ethanol to represent the cachaça, since it is a sugarcane liquor.
- sugar > To represent the sugar, I will use glucose, since it is a simple sugar and is commonly used in drinks.

Temperatures:
- Room temperature: 298.15 K (25 °C)
- Freezer temperature: 273 K (0 °C)

Mixture properties to estimate: 
- Molar mass
- Rho (density)
- Heat capacity
- Thermal conductivity
- Prandtl number

Composition of the mixture (mass fraction):
- water = 0.5
- ethanol = 0.4
- glucose = 0.1

Represented as a array: array[water, ethanol, glucose]
"""
####################################################################################################################
# Libs
from thermo.chemical import Chemical
from thermo.chemical import Mixture


####################################################################################################################
# Constants

# Temperatures
rommT = 298.15 # K
freezerT = 273 # K

# Composition (mass fraction)
composition = [0.4, 0.4, 0.1] # water, ethanol, glucose

####################################################################################################################
# Functions
def draw(): # Just a function to make the terminal prettier =) (and faster to print LOL)
    print()
    print("___" * 30)
    print()
####################################################################################################################
draw()
print("Lab - Booze?")
print("By: Alison Likoski Neves")
draw()

# Creating the mixture

# 298.15 K (room temperature)
caipirinhaRommT = Mixture(["water", "ethanol", "glucose"], ws = composition, T = rommT)

# 273 K (freezer temperature)
caipirinhaFreezerT = Mixture(["water", "ethanol", "glucose"], ws = composition, T = freezerT)

# Comparing the properties of the mixture at room temperature and freezer temperature
# Molar mass, density, heat capacity, thermal conductivity, Prandtl number

print("Mixture properties of Caipirinha at room temperature (25 C) and freezer temperature (0 C):")
print("Properties                   | Room temperature (25 C) | Frezeer temperature (0 C)" )
print("---" * 30)
print("Molar massa (g/mol)          | ", caipirinhaRommT.MW, "      |  ", caipirinhaFreezerT.MW)
print("Density (kg/m³)              | ", caipirinhaRommT.rho, "     |  ", caipirinhaFreezerT.rho)
print("Heat capacity (J/kg.K)       | ", caipirinhaRommT.Cp, "     |  ", caipirinhaFreezerT.Cp)
print("Thermal conductivity (W/m.K) | ", caipirinhaRommT.k, "   |  ", caipirinhaFreezerT.k)
print("Prandtl number (dimens.less) | ", caipirinhaRommT.Pr, "     |  ", caipirinhaFreezerT.Pr)
print("---" * 30)





