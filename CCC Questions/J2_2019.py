list = []

k = int(input())
for i in range(0,k,1):
	i = input()
	i = int(i[0])*str(i[2])
	list.append(i)
	
for i in range(0,k,1):
	print(list[i])