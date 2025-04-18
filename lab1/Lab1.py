"""
Lab 1 - Problem 3 - Areas and Volume of a Sphere

PosEnq UFSC
Alison Likoski Neves

"""
import math

# Ask radius

radius = float(input("Insert the radius value: "))

# Calculate the values of Area and Volume

sphArea = 4 * math.pi * (radius ** 2)
sphVol = 4 / 3 * math.pi * (radius**3)

# Display the values to user

print(f"The value of area is: {sphArea}")
print(f"The value of volume is: { sphVol}")