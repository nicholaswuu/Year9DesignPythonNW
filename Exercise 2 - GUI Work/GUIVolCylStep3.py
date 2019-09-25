import math
import tkinter as tk

def calcVolCylinder(radius,height):

	if (radius >= 0 and height >= 0):
		volume = math.pi*math.pow(radius, 2)*height
		volume = round(volume, 2)
		return volume 
	else:
		return ("Error! Positive Values Only!")

def runMe(*args):
	r = radiusEntry.get()
	r = float(r)
	radiusEntry.delete(0,tk.END)

	h = heightEntry.get()
	h = float(h)
	heightEntry.delete(0,tk.END)

	print("Runnning...")
	volume = calcVolCylinder(r,h)
	print(volume)
	output.config(state = "normal")
	output.delete(0,tk.END)
	result = "\n\n\tr\t= "+str(r)+" units\n\th\t= "+str(h)+" units\n\tvolume\t= "+str(volume)+" units\u00B3"
	output.insert(tk.END, result)
	output.config(state="disabled")
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
btnrun.config(fg="blue", command = runMe)
btnrun.pack(fill = tk.BOTH)

check = tk.Checkbutton(root, text = "High Contrast")
check.config(anchor = tk.W)
check.pack(fill = tk.BOTH)

root.bind("<Return>",runMe)
root.mainloop()
print("End Program")