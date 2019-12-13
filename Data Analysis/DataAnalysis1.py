data = open("dataAnalysis1.txt","r");
dataString = data.read()


dataList = dataString.split("\n")

for i in range(0, len(dataList), 1):
	dataList[i] = dataList[i].replace(",","")
	dataList[i] = float(dataList[i])

minimum = min(dataList)
print(minimum)

maximum = max(dataList)
print(maximum)

diff = maximum - minimum
print(diff)

smallest = dataList[0]
for i in range (0, len(dataList), 1):
	if smallest > dataList[i]:
		smallest = dataList[i]

print("MIN IS: " + str(smallest))

largest = dataList[0]
for i in range (0, len(dataList), 1):
	if largest < dataList[i]:
		largest = dataList[i]

print("MAX IS: " + str(largest))


maxvalue = input("What number do you want to set as upper limit: ")
maxvalue = float(maxvalue)
biggest = dataList[0]
minvalue = input("What number do you want to set as lower limit: ")
minvalue = float(minvalue)
smallest1 = dataList[0]

for i in range (0, len(dataList), 1):
	if maxvalue > dataList[i] and dataList[i] > biggest:
		biggest = dataList[i]

print("MAX IS: " + str(biggest))

for i in range (0, len(dataList), 1):
	if minvalue < dataList[i] < smallest1:
		smallest1 = dataList[i]

print("MIN IS: " + str(smallest1))

