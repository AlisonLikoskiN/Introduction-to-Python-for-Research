"""
PosENQ - UFSC
Introduction to python to research - ENQ410034
Alison Likoski Neves - 202405086
Lab 6: matplotlib
"""
####################################################################################################################
"""
Problem 4 - Sassy Scattergram
Choose a scientific article and reproduce a scatter-line plot, displaying several data (at least three different data sets)
using customized colors, legend, and markers. 
Make it more remarkable than the original. Put both on your report for reference.
####################################################################################################################
Article choosen: Parametric design of curved hydrocyclone using data points and its separation enhancement mechanism
https://doi.org/10.1016/j.cep.2024.110043
Image for reference: Fig. 15. Grading efficiency plots of the experiment for different curve type hydrocyclones.
"""
####################################################################################################################
# Libs
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

####################################################################################################################
# Data
# H1
xH1 = [
    4.017278618,
    10.10799136,
    16.45788337,
    22.80777538,
    28.76889849,
    35.24838013,
    41.20950324,
    47.68898488,
    53.90928726,
    60.0
]
yHi =  [
    2.209944751,
    25.69060773,
    36.1878453,
    47.23756906,
    60.77348066,
    70.44198895,
    78.45303867,
    80.66298343,
    82.87292818,
    89.22651934
]

# H2
xH2 = [
    4.276457883,
    10.10799136,
    16.45788337,
    22.67818575,
    28.89848812,
    35.1187905,
    41.20950324,
    47.30021598,
    54.03887689,
    60.0
]

yH2 = [
    8.563535912,
    24.30939227,
    41.43646409,
    58.01104972,
    70.71823204,
    82.87292818,
    90.05524862,
    94.19889503,
    93.92265193,
    95.3038674
]

# H3
xH3 =  [
    3.887688985,
    10.23758099,
    16.71706263,
    22.41900648,
    28.89848812,
    34.98920086,
    41.20950324,
    47.55939525,
    53.77969762,
    59.87041037
]

yH3 = [
    3.867403315,
    31.7679558,
    46.96132597,
    60.22099448,
    72.09944751,
    79.83425414,
    89.22651934,
    94.75138122,
    95.85635359,
    95.3038674
]


####################################################################################################################
# Functions
def draw(): # Just a function to make the terminal prettier =) (and faster to print LOL)
    print()
    print("___" * 30)
    print()


####################################################################################################################
draw()
print("Lab - Sassy Scattergram.")
print("By: Alison Likoski Neves")
draw()

# Creating the scatter line plot
plt.scatter(xH1, yHi, color = 'darkviolet', label = 'H1', marker = 'o')
plt.scatter(xH2, yH2, color = 'lime', label = 'H2', marker = '8')
plt.scatter(xH3, yH3, color = 'red', label = 'H3', marker = 'v' )
plt.plot(xH1, yHi, color = 'darkviolet', linestyle = 'dotted', alpha = 0.9)
plt.plot(xH2, yH2, color = 'lime', alpha = 0.7)
plt.plot(xH3, yH3, color = 'red', linestyle = 'dashed', alpha = 0.5)

plt.xlabel('diameter (um)')
plt.ylabel('Grading efficiency (%)')
plt.legend()
plt.show()
####################################################################################################################
