N = int(input())

listx = []
listy = []

for i in range(N):
	i = input()
	if len(i) == 4:
		try:
			listx.append(int(i[0:1]))
			listy.append(int(i[2:4]))
		except:
			listx.append(int(i[0:2]))
			listy.append(int(i[3:4]))
	if len(i) == 5:
		try:
			listx.append(int(i[0:2]))
			listy.append(int(i[3:5]))
		except:
			listx.append(int(i[0:1]))
			listy.append(int(i[2:5]))
		finally:
			listx.append(int(i[0:3]))
			listy.append(int(i[4:5]))
	if len(i) == 6:
		try:
			listx.append(int(i[0:3]))
			listy.append(int(i[4:6]))
		except:
			listx.append(int(i[0:2]))
			listy.append(int(i[3:6]))
	if len(i) == 7:
		listx.append(int(i[0:3]))
		listy.append(int(i[4:7]))

bigx = 0
smallx = listx[0]
bigy = 0
smally = listy[0]

for i in range(0,len(listx),1):
	if listx[i]>bigx:
		bigx = int(listx[i])
	if listx[i]<smallx:
		smallx = int(listx[i])

for i in range(0,len(listy),1):
	if listy[i]>bigy:
		bigy = int(listy[i])
	if listy[i]<smally:
		smally = int(listy[i])

print(str(smallx-1) + "," + str(smally-1))
print(str(bigx+1) + "," + str(bigy+1))