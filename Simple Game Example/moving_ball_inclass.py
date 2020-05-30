from tkinter import *
from random import randint

def moveball():
	print("BALL MOVING")
	dx = 1
	dy = 1
	canvas.move(ball1, dx, dy)
	canvas.move(ball2, -1*dx, -1*dy)
	root.after(10, moveball)

root = Tk()
root.title("Moving Balls")
root.resizable(False,False);

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()
ball1 = canvas.create_oval(10,10,20,20, fill = "red")
ball2 = canvas.create_oval(210,210,220,220, fill = "red")

root.after(10,moveball)

root.mainloop()
print("TERMINATE GAME")