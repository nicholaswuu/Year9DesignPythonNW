import math

def calcVolCylinder(radius,height):

	if (radius >= 0 and height >= 0):
		volume = math.pi*math.pow(radius, 2)*height
		volume = round(volume, 2)
		return volume 
	else:
		return -1

#MAIN CODE
print("Start Program")
result = calcVolCylinder(4,3)
print(result)
print("End Program")