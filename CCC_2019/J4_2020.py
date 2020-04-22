T = input()
S = input()
list = []
for i in range(0, len(T), 1):
	for j in range(0, len(S), 1):
		if T[0+i:i+len(S)] == S[j:]+S[0:j]:
			list.append("yes")
			break
if len(list) >= 1:
	print("yes")
else:
	print("no")