limit = input("Enter the speed limit: ")
speed = input("Enter the recorded speed of the car: ")
limit = int(limit)
speed = int(speed)

if (speed<=limit):
	print("Congratulations, you are within the speed limit!")
elif (0<speed-limit<=20):
	print("You are speeding and your fine is $100.")
elif (20<speed-limit<=30):
	print("You are speeding and your fine is $270.")
elif (30<speed-limit):
	print("You are speeding and your fine is $500.")