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
	global m, y, numdays, startofmonth
	m = m - 1
	if(m == 0):
		m = 12
		y-=1
	numdays = monthrange(y,m)[1]
	startofmonth = monthrange(y,m)[0]
	resetHeader()
	resetCal()

def nextmonth():
	global m, y, numdays, startofmonth
	m = m + 1
	if(m == 13):
		m = 1
		y+=1
	numdays = monthrange(y,m)[1]
	startofmonth = monthrange(y,m)[0]
	resetHeader()
	resetCal()

def resetHeader():
	global title, prev, nextm, header
	header.grid_forget()
	header = tk.LabelFrame(root, bd = 0)
	header.grid(row=0, column = 4, sticky="n")

	prev = tk.Button(header, text = "<", font = ("Roboto",35), fg = "black", width = 3, command = prevmonth)
	title = tk.Label(header, text = months[m-1] + " " + str(y), font = ("Roboto",35), width = 45)
	nextm = tk.Button(header, text = ">", font = ("Roboto",35), fg = "black", width = 3, command = nextmonth)

	prev.grid(row = 0, column = 0, sticky = "w")
	nextm.grid(row = 0, column = 2, sticky = "e")
	title.grid(row = 0, column = 1, pady = 15)

def resetCal():
	global cal, m, y, numdays, startofmonth
	cal.grid_forget()
	cal = tk.LabelFrame(root, bd = 0)
	cal.grid(row=1, column = 4, sticky="n")
	for i in range(0, len(weekdays), 1):
		labels = tk.Label(cal, text = weekdays[i], width = 15, bg = "grey80")
		labels.grid(row = 1, column = i+1, padx = 5, pady = 5)

	for i in range(1, numdays+1, 1):
		dayofweek = (i+startofmonth)%7
		if(i == d and m == datetime.now().month and y == datetime.now().year):
			date = tk.Label(cal, text = str(i), anchor = "n", width = 15, height = 6, fg = "black", bg = "grey90")
		else:
			date = tk.Label(cal, text = str(i), anchor = "n", width = 15, height = 6)
		date.grid(row = (i+startofmonth)//7+2, column = dayofweek+1, padx = 5, pady = 5)


root = tk.Tk()

header = tk.LabelFrame(root, bd = 0)
header.grid(row=0, column = 0, columnspan = 8, sticky="n")

cal = tk.LabelFrame(root, bd = 0)
cal.grid(row=1, column = 0, columnspan= 8, sticky="n")

#******************** CALENDAR *********************

for i in range(0, len(weekdays), 1):
	labels = tk.Label(cal, text = weekdays[i], width = 15, bg = "grey80")
	labels.grid(row = 1, column = i+1, padx = 5, pady = 5)

for i in range(1, numdays+1, 1):
	dayofweek = (i+startofmonth)%7
	if(i == d and m == datetime.now().month):
		date = tk.Label(cal, text = str(i), anchor = "n", width = 15, height = 6, fg = "black", bg = "grey90")
	else:
		date = tk.Label(cal, text = str(i), anchor = "n", width = 15, height = 6)
	date.grid(row = (i+startofmonth)//7+2, column = dayofweek+1, padx = 5, pady = 5)

#******************** TITLE *********************

prev = tk.Button(header, text = "<", font = ("Roboto",35), fg = "black", width = 3, command = prevmonth)
title = tk.Label(header, text = months[m-1] + " " + str(y), font = ("Roboto",35), width = 45)
nextm = tk.Button(header, text = ">", font = ("Roboto",35), fg = "black", width = 3, command = nextmonth)

prev.grid(row = 0, column = 0)
nextm.grid(row = 0, column = 2)
title.grid(row = 0, column = 1, pady = 15)

root.mainloop()