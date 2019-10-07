import tkinter as tk

print("Start Program")
root = tk.Tk()

root.title("A Widget")

ctx=tk.Canvas(root, width = 300, height = 100, bg = "blue")
ctx.config()
ctx.pack()

root.mainloop()

print("END PROGRAM")