A3 = int(input())
A2 = int(input())
A1 = int(input())
B3 = int(input())
B2 = int(input())
B1 = int(input())

Apple = 3 * A3 + 2 * A2 + A1
Banana = 3 * B3 + 2 * B2 + B1

if Apple < Banana:
	print("B")

if Apple > Banana:
	print("A")

if Apple == Banana:
	print("T")