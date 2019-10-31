import tkinter as tk

root = tk.Tk()

button = tk.Button(root, text = "Conjugate")
button.config(fg = "green", width = 25, height=2)
button.pack()

verbEntry = tk.Entry(root)
verbEntry.config(width = 100)
verbEntry.pack()

root.mainloop()