import calendar as c
from calendar import monthrange
import tkinter as tk

y = int(input("Year: "))
m = int(input("Month: "))

numdays = monthrange(y,m)[1]
startofmonth = monthrange(y,m)[0]

counter = 0

mon = []
tue = []
wed = []
thu = []
fri = []
sat = []
sun = []


for i in range(1, numdays+1, 1):
	dayofweek = (i+startofmonth-1)%7

	if(dayofweek == 0):
		mon.append(i)
	if(dayofweek == 1):
		tue.append(i)
	if(dayofweek == 2):
		wed.append(i)
	if(dayofweek == 3):
		thu.append(i)
	if(dayofweek == 4):
		fri.append(i)
	if(dayofweek == 5):
		sat.append(i)
	if(dayofweek == 6):
		sun.append(i)

print(mon)
print(tue)
print(wed)
print(thu)
print(fri)
print(sat)
print(sun)


#root = tk.Tk()

#calendar = c.TextCalendar(c.SUNDAY)
#cal_content = calendar.formatmonth(2020,5)
#cal_year = tk.Label(root, text = cal_content, anchor = "e", justify = "right") 
#cal_year.pack()

#root.mainloop()