"""
PosENQ - UFSC
Introduction to python to research - ENQ410034
Alison Likoski Neves - 202405086
Lab 6: matplotlib
"""
####################################################################################################################
"""
Problem 2 - Skill Pills Thrills Drills
Make one plot for each type of the following types:
- Scatter
- Line-Scatter
- Pie
- Bars
- Histogram
- Boxplot
- Contour Plot

"""
####################################################################################################################
# Libs
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

####################################################################################################################
# Constants


####################################################################################################################
# Functions
def draw(): # Just a function to make the terminal prettier =) (and faster to print LOL)
    print()
    print("___" * 30)
    print()


def randomArray(n): # Creates a random array with random numbers for a random graph LOL 
    return np.random.rand(n) # I know it doesnt make much sense creating a function just for this, but I like to create functions

def arraySum1(n): # Creates a random array but the sum of the numbers need to be = 1
  numbers = randomArray(n) # Creates a random array using the function randomArray
  sum = np.sum(numbers) # Normalization, sum of all numbers
  array1 = numbers / sum # Normalization, divides the number by the sum of the numbers
  return array1
  
def randomLabels(n, name): # Function to make a array of random labels, made to Pie chart, but probably gonna use for others plots
  labels = [''] * numbersOfData 
  for i in range(n):
    labels[i] = 'Random ' + name + ' ' + str(i + 1) # Naming all the labels as Random + plot name + number, (I'm not a creative person, so I prefer do all random data)
  return labels

####################################################################################################################

draw()
print("Lab - Skill Pills Thrills Drills")
print("By: Alison Likoski Neves")
draw()

####################################################################################################################
# Scatter plot
print("Scatter plot:")
# Creating x and y
scatterX = randomArray(20)
scatterY = randomArray(20)
# Ploting
plt.scatter(scatterX, scatterY, marker = 'v', color = 'darkviolet')
plt.xlabel('Random X')
plt.ylabel('Random Y')
plt.title('Random scatter plot')
#Finish and show the graph
plt.show()
draw()

####################################################################################################################

# Line- Scatter plot
print('Line Scatter plot:')
# Creating x and y
lineSctX = np.linspace(0, 20, 51)
lineSctY = randomArray(51)
lineSctY2 = randomArray(51)
# Ploting
plt.plot(lineSctX, lineSctY, marker = 'D', color = 'lime', linestyle = 'dotted', label = 'Random in lime')
plt.plot(lineSctX, lineSctY2, marker = 'o', color = 'navy', linestyle = 'dashed', label = 'Random in navy')
plt.xlabel('Random X')
plt.ylabel('Random Y')
plt.title('Random line scatter plot')
plt.legend()
#Finish and show the graph
plt.show()
draw()

####################################################################################################################

# Pie  plot
print('Pie plot:')
# Creating data
numbersOfData = random.randint(2, 10) # Creates the number of data to pie chart
pieRandomData = arraySum1(numbersOfData) # Get the values
labels = randomLabels(numbersOfData, 'Pie') # Get the labels
# Right here I forgot about the colors, and I'm too lazy to make a array with all the color names, are you even reading this?
plt.pie(pieRandomData, labels = labels, startangle = 90) # Creating the pie chart
plt.title("A random pie chart of random numbers, saying (not so) random things!") # A fancy title
plt.show() # Finishin and ploting
draw()

####################################################################################################################

# Bars plot
print('Bars plot:')
categories = randomLabels(numbersOfData, 'Bars') # Get the labels
barsRandomData = arraySum1(numbersOfData) * 100 # Get the values
# Creating bar plot
plt.bar(categories, barsRandomData)
plt.xticks(rotation = 90) # Rotating the labels, making it possible to read
plt.xlabel('Random categories')
plt.ylabel('Random values')
plt.title('Random bars plot')
plt.show()
draw()

####################################################################################################################

# Histogram
print('Histogram:')
histogramData = np.random.normal(size = 100) # Creates random data
plt.hist(histogramData, bins = numbersOfData, color= 'darkviolet', alpha = 0.75) # Ploting
plt.xlabel('Random values')
plt.ylabel('Frequency')
plt.title('Random histogram')
plt.show()
draw()

####################################################################################################################

# Boxplots 
print('Boxplots:')
boxplotData = [np.random.normal(0, i, 100) for i in range(1,4)]

plt.boxplot(boxplotData, vert = False , patch_artist= True, boxprops= dict(facecolor = 'darkviolet', color = 'lime'))
plt.xlabel('Random values')
plt.ylabel('Frequency')
plt.title('Random boxplot')
plt.show()
draw()

####################################################################################################################

# Contour plots
print('Contour plots:')
ctPlotx = np.linspace(-10, 15, 100)
ctPloty = np.linspace(-2, 23, 100)
ctPlotX, ctPlotY = np.meshgrid(ctPlotx, ctPloty)

ctPlotZ = ctPlotX + np.sin(ctPlotY) + ctPlotY 

plt.contour(ctPlotX, ctPlotY, ctPlotZ, colors = 'darkviolet')
plt.contourf(ctPlotX, ctPlotY, ctPlotZ, cmap = 'jet')
plt.xlabel('Random X')
plt.ylabel('Random Y')
plt.title('Random contour plot of x + sin(y) + y (A fancy wavy plot)')
plt.show()
draw()

####################################################################################################################