import tkinter as tk

def motion(event):
	print("Mouse position: (%s %s)" % (event.x,event.y))
	return

print("Start");
root = tk.Tk()

canvas = tk.Canvas(root, width=300, height = 300)
canvas.pack()

canvas.create_rectangle(120,100,180,200,fill = "grey")

canvas.bind("<Motion>",motion)

root.mainloop();
print("End")