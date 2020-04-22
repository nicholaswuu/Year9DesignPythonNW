import tkinter as tk

print("Start");
root = tk.Tk()

canvas = tk.Canvas(root, width=300, height = 300)
canvas.pack()


canvas.create_oval(220, 90, 245, 115, outline = "#fff", fill="#000", width=2)
canvas.create_oval(100, 90, 125, 115, outline = "#fff",fill="#000", width=2)
canvas.create_rectangle(75,50,225,100,fill = "yellow")
canvas.create_rectangle(225,75,250,100,fill = "yellow")
canvas.create_oval(210, 95, 235, 120, outline = "#fff", fill="#000", width=2)
canvas.create_oval(90, 95, 115, 120, outline = "#fff",fill="#000", width=2)

root.mainloop();