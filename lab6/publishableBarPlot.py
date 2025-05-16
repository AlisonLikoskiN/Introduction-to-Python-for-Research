"""
PosENQ - UFSC
Introduction to python to research - ENQ410034
Alison Likoski Neves - 202405086
Lab 6: matplotlib
"""
####################################################################################################################
"""
Problem 3 - Publishable Bar Plot.
Choose a scientific article with three categories in a bar figure, reproduce the bar plot using customized colors
and legend, and use other hash options. Put both on your report for reference.

####################################################################################################################

Article name: Optimization of involute feed hydrocyclone for enhanced mud removal: Synergistic analysis of flow dynamics and separation efficiency
https://doi.org/10.1016/j.mineng.2025.109376
Image for reference: Fig. 9. Separation performance of the cyclones with different feed bodies.
"""
####################################################################################################################
# Libs
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

####################################################################################################################
# Data from article bar plot
Usr = [90.65, 92.19, 93.72, 92.84, 95.04]
Us = [82.98, 84.95, 87.58, 86.27, 88.90]
E = [82.76, 82.32, 83.20, 80.13, 84.73]
Umr = [ 56.90, 50.32, 40.46, 43.97, 35.64]
Um = [17.23, 15.04, 12.41, 13.94, 11.09]

# Bar width
barWidth = 0.25



####################################################################################################################
# Functions
def draw(): # Just a function to make the terminal prettier =) (and faster to print LOL)
    print()
    print("___" * 30)
    print()


####################################################################################################################
draw()
print("Lab - Publishable Bar Plot.")
print("By: Alison Likoski Neves")
draw()

# Positions of the bars on x-axis
r1 = np.arange(len(Usr))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]

# Creating the categories, combining the same index from samples
labels = [ "T", "A", "H", "TC", "I" ]
categories_data = []

for i in range(len(labels)):
  categories_data.append([Usr[i], Us[i], E[i], Umr[i], Um[i]])

# Creating the bar plot
plt.bar(r1, categories_data[0], color = 'blue', width= barWidth, edgecolor = 'black', label = labels[0], hatch ='/')
plt.bar(r2, categories_data[1], color = 'green', width= barWidth, edgecolor = 'black', label = labels[1], hatch='\\')
plt.bar(r3, categories_data[2], color = 'red', width= barWidth, edgecolor = 'black', label = labels[2], hatch='.')
plt.bar(r4, categories_data[3], color = 'orange', width= barWidth, edgecolor = 'black', label = labels[3], hatch='x')

plt.xticks([r + barWidth for r in range(len(Usr))], labels)
plt.legend()

plt.ylabel('Numerical Value %')
plt.xlabel('Feed body structure')
plt.show()
####################################################################################################################
