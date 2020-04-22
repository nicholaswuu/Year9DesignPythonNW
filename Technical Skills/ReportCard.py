nums = 12
marks = "ABCFFDFFAABA"
ctr = 0

for i in range(0,nums):
	if(marks[i]=="A"):
		ctr = ctr+1

print(ctr)