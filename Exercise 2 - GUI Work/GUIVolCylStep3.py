import math
import tkinter as tk

def calcVolCylinder(radius,height):

	if (radius >= 0 and height >= 0):
		volume = math.pi*math.pow(radius, 2)*height
		volume = round(volume, 2)
		return volume 
	else:
		return -1
		
def runMe():
  print("Runnning")
#MAIN CODE
root = tk.Tk()
#Building widgets goes before mainloop.
title = tk.Label(root, text = "Cylinder Volume Calculator")
title.config(fg = "white", bg = "black") 
title.pack(fill = tk.BOTH)

radiusLabel = tk.Label(root, text = "Radius:")
radiusLabel.config(anchor = tk.W)
radiusLabel.pack(fill = tk.BOTH)

radiusEntry = tk.Entry(root)
radiusEntry.config()
radiusEntry.pack(fill = tk.BOTH)

heightLabel = tk.Label(root, text = "Height:")
heightLabel.config(anchor = tk.W)
heightLabel.pack(fill = tk.BOTH)

heightEntry = tk.Entry(root)
heightEntry.config()
heightEntry.pack(fill = tk.BOTH)

output = tk.Text(root)
output.config(width = 50, height = 10, state = "disabled", borderwidth = 2, relief = "groove")
output.pack()

btnrun = tk.Button(root, text = "CALCULATE", highlightbackground='#8e96ab')
btnrun.config(fg="blue")
btnrun.pack(fill = tk.BOTH)

check = tk.Checkbutton(root, text = "High Contrast")
check.config(anchor = tk.W)
check.pack(fill = tk.BOTH)

root.mainloop()
print("End Program")