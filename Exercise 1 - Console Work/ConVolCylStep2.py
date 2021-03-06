import math

print("\nThis program will find the volume by using the radius and height")
print("\nVolume of a Cylinder Formula: ")
print("\n\tLet r = radius and h = height")
print("\n\tVolume = \u03C0r\u00b2h")


#Input
#What inputs are needed to calculate the volume of a cylinder?
#Radius and height

print("\nInput: ")
name = input("\n\tWhat is your name: ")

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