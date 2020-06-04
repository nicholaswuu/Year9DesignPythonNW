from calendar import monthrange
import tkinter as tk
from datetime import datetime
import tkinter.ttk

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
	header.grid(row=0, column = 0, sticky="n")

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
	cal.grid(row=1, column = 0, sticky="n")
	for i in range(0, len(weekdays), 1):
		labels = tk.Label(cal, text = weekdays[i], width = 15, bg = "grey80")
		labels.grid(row = 1, column = i+1, padx = 5, pady = 5)

	for i in range(1, numdays+1, 1):
		dayofweek = (i+startofmonth)%7
		if(i == d and m == datetime.now().month and y == datetime.now().year):
			date = tk.Label(cal, text = str(i), anchor = "n", width = 15, height = 6, fg = "black", bg = "grey90")
		else:
			date = tk.Label(cal, text = str(i), anchor = "n", width = 15, height = 6, bg = "grey98")
		date.grid(row = (i+startofmonth)//7+2, column = dayofweek+1, padx = 5, pady = 5)

def newtask():
	global sidebar, sidebar2
	sidebar.grid_forget()
	sidebar2.grid(row=0, rowspan = 2, column = 1, sticky="n")

def addcancel():
	global sidebar, sidebar2
	sidebar2.grid_forget()
	sidebar.grid(row=0, rowspan = 2, column = 1, sticky="n")

def addsave():
	global sidebar, sidebar2
	sidebar2.grid_forget()
	sidebar.grid(row=0, rowspan = 2, column = 1, sticky="n")

root = tk.Tk()

header = tk.LabelFrame(root, bd = 0)
header.grid(row=0, column = 0, sticky="n")

cal = tk.LabelFrame(root, bd = 0)
cal.grid(row=1, column = 0, sticky="n")

sidebar = tk.LabelFrame(root, bd = 0)
sidebar.grid(row=0, rowspan = 2, column = 1, sticky="n")

sidebar2 = tk.LabelFrame(root, bd = 0)

#******************** HEADER *********************

prev = tk.Button(header, text = "<", font = ("Roboto",35), fg = "black", width = 3, command = prevmonth)
title = tk.Label(header, text = months[m-1] + " " + str(y), font = ("Roboto",35), width = 45)
nextm = tk.Button(header, text = ">", font = ("Roboto",35), fg = "black", width = 3, command = nextmonth)

prev.grid(row = 0, column = 0)
nextm.grid(row = 0, column = 2)
title.grid(row = 0, column = 1, pady = 15)

#******************** CALENDAR *********************

for i in range(0, len(weekdays), 1):
	labels = tk.Label(cal, text = weekdays[i], width = 15, bg = "grey80")
	labels.grid(row = 1, column = i+1, padx = 5, pady = 5)

for i in range(1, numdays+1, 1):
	dayofweek = (i+startofmonth)%7
	if(i == d and m == datetime.now().month):
		date = tk.Label(cal, text = str(i), anchor = "n", width = 15, height = 6, fg = "black", bg = "grey90")
	else:
		date = tk.Label(cal, text = str(i), anchor = "n", width = 15, height = 6, bg = "grey98")
	date.grid(row = (i+startofmonth)//7+2, column = dayofweek+1, padx = 5, pady = 5)

#******************** SIDEBAR *********************

head = tk.Label(sidebar, text = "Tasks", font = ("Roboto",25), width = 15, height = 2, bg = "#e0eefa")
taskbtn = tk.Button(sidebar, text = "Add Task", bg = "#e0eefa", width = 15, height = 2, command = newtask)
head.grid(row = 0, padx = 10, pady = 15)
taskbtn.grid(row = 1, padx = 10, pady = 15, sticky = "s")

addtaskhead = tk.Label(sidebar2, text = "New Task", font = ("Roboto",25), width = 15, height = 2, bg = "#e0eefa")
tasknamelabel = tk.Label(sidebar2, text = "Task Name:", font = ("Roboto", 15))
taskname = tk.Entry(sidebar2, width = 25)
datelabel = tk.Label(sidebar2, text = "Date (DD/MM/YYYY): ", font = ("Roboto", 15))
datesetD = tk.Entry(sidebar2, width = 3)
slash = tk.Label(sidebar2, text = "/", font = ("Roboto", 15))
datesetM = tk.Entry(sidebar2, width = 3)
slash2 = tk.Label(sidebar2, text = "/", font = ("Roboto", 15))
datesetY = tk.Entry(sidebar2, width = 5)

cancelbtn = tk.Button(sidebar2, text = "Cancel", bg = "#e0eefa", width = 12, height = 2, command = addcancel)
addbtn = tk.Button(sidebar2, text = "Add", bg = "#e0eefa", width = 12, height = 2, command = addsave)

addtaskhead.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 15)
tasknamelabel.grid(row = 1, column = 0, columnspan = 2, padx = 10, pady = (0,10), sticky = "w")
taskname.grid(row = 2, column = 0, columnspan = 2, padx = 10, pady = (0,10))
datelabel.grid(row = 3, column = 0, columnspan = 2, padx = 10, pady = 10, sticky = "w")
datesetD.grid(row = 4, column = 0, padx = 10, pady = (0,10), sticky = "w")
slash.grid(row = 4, column = 0, pady = (0,10))
datesetM.grid(row = 4, padx = 15, pady = (0,10), column = 0, sticky = "e")
slash2.grid(row = 4, column = 0, pady = (0,10), sticky = "e")
datesetY.grid(row = 4, column = 1, pady = (0,10), sticky = "w")
cancelbtn.grid(row = 8, column = 0, pady = 15, sticky = "sw")
addbtn.grid(row = 8, column = 1, padx = 10, pady = 15, sticky = "se")

root.mainloop()