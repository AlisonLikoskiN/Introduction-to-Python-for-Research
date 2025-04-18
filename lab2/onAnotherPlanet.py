"""
PosENQ - UFSC
Introduction to python to research - ENQ410034
Alison Likoski Neves - 202405086
Lab 2: Booleans, Conditionals, and Loops
"""
####################################################################################################################
"""
Problem 4 - On another planet
NASA has hired you to develop a shot Python script that, when run, asks the user to enter their weight on Earth and select the playent they are currently on.
The program must then calculate and print on the screen the individual`s weight on the desired planet.
Use a relative weight table like the one below to simplify the calculator.
"""
####################################################################################################################

# Lists

planets = ["mercury","venus","earth","mars","jupiter","saturn","uranus","neptune"]
relativeWeights = [0.38, 0.91, 1.0, 0.38, 2.34, 1.06, 0.92, 1.19]

####################################################################################################################

# Functions

# Getting the earth weight (a positive number...)

def getWeight():
    # Get the weight
    # Check if it`s a positive value
    # Return the weight
    weight = -1
    while weight < 0:
        weight = float(input())
        if weight < 1:
            print("Please, insert a valid positive value")
        else:
            return weight

# Getting the desired planet (a valid planet ...)

def getPlanet():
    # Get the planet
    # Check if the planet is on the list
    # Return the name
    while True:
        planet = input().lower() # normalize the chars
        if planet in planets: # If the name is on the list, return the name
            return planet
        else: # If not on the list, ask again and inform valid options
            print("____"*10)
            print("Please, insert a valid planet.")
            print("Valid planets are:")
            for i in planets:
                print(i)
            print("____"*10)

####################################################################################################################

# Calculator code

print("____"*10)
print("NASA weight calculator.")
print("____"*10)

# Getting the weight on Earth using the getWeight function 
print("Please, insert your weight on Earth: ")
originalWeight = getWeight()
print("____"*10)

# Getting the desired planet using the getPlanet function
print("Please, insert the desired planet:")
desiredPlanet = getPlanet()
print("____"*10)

# Getting the index of planet in the planets list to use on gravity list and calculate the new weight
i = planets.index(desiredPlanet)

# Using the index to get the gravity factor and calculates the weight
newWeight = originalWeight * relativeWeights[i]

# Displays to the user
print(f"The new weight on {planets[i]} is {newWeight}")
print("____"*10)
