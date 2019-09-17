import math

print("\nVolume of a Cylinder Formula: ")
print("\nVolume = \u03C0 \u00d7 radius\u00b2 \u00d7 height")
#Input
#What inputs are needed to calculate the volume of a cylinder?
#Radius and height

name = input("\nWhat is your name: ")

radius = input("\n\tInput radius(cm): ")
radius = (int)(radius)

height = input("\n\tInput height(cm): ")
height = (int)(height)


#Process
#What formula is used to calculate the volume of a cylinder?
#Volume = pi * radius * radius * height
volume = math.pi*math.pow(radius, 2)*height
volume = round(volume, 2)

#Output
#What is important about the output?

print("\nHi "+name+"!")
print("\nGiven a cylinder with:")
print("\n\tRadius = "+str(radius))
print("\n\tHeight = "+str(height))
print("\nThe volume is: "+str(volume)+"\n")  