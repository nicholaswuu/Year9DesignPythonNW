from calendar import monthrange
import tkinter as tk
from datetime import datetime

d = datetime.now().day
m = datetime.now().month
y = datetime.now().year

weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

numdays = monthrange(y,m)[1]
startofmonth = monthrange(y,m)[0]

def prevmonth():
	global m
	m = m - 1
	if(m == 0):
		m = 12
	print(m)

def nextmonth():
	global m, y
	m = m + 1
	if(m == 13):
		m = 1
	print(m)


root = tk.Tk()

#******************** CALENDAR *********************

for i in range(0, len(weekdays), 1):
	labels = tk.Label(root, text = weekdays[i], width = 15, bg = "grey80")
	labels.grid(row = 1, column = i+1, padx = 5, pady = 5)

for i in range(1, numdays+1, 1):
	dayofweek = (i+startofmonth)%7
	if(i == d and m == datetime.now().month):
		date = tk.Label(root, text = str(i), anchor = "n", width = 15, height = 6, fg = "black", bg = "grey90")
	else:
		date = tk.Label(root, text = str(i), anchor = "n", width = 15, height = 6)
	date.grid(row = (i+startofmonth)//7+2, column = dayofweek+1, padx = 5, pady = 5)

#******************** TITLE *********************

prev = tk.Button(root, text = "<", font = ("Roboto",35), fg = "black", width = 3, command = prevmonth)
title = tk.Label(root, text = months[m-1] + " " + str(y), font = ("Roboto",35))
nextm = tk.Button(root, text = ">", font = ("Roboto",35), fg = "black", width = 3, command = nextmonth)

prev.grid(row = 0, column = 1)
nextm.grid(row = 0, column = 7)
title.grid(row = 0, column = 4, pady = 15)

root.mainloop()