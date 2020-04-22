P = int(input())
N = int(input())
R = int(input())
spread = 0
list = []

for i in range(0,2000,1):
	spread = spread + N*pow(R,i)
	if P<spread:
		list.append(i)

print(list[0])