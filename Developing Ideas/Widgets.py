import tkinter as tk

root = tk.Tk()

textbox = tk.Text(root)#Textbox to place outputs and examples.
textbox.config(width = 100, height = 5)	
textbox.pack()
textbox.insert(tk.END, "Basic widgets that will be used in this program")

verbEntry = tk.Entry(root)	#Entry box, will be used for verb and pronoun
verbEntry.config(width = 100)
verbEntry.pack()

button = tk.Button(root, text = "Conjugate")	#Button, will be used to do the conjugation, and for audio
button.config(fg = "green", width = 25, height=2)
button.pack(pady=30)

check = tk.Checkbutton(root, text = "High Contrast")	#Checkbox for high contrast
check.config(anchor = tk.W)
check.pack(fill = tk.BOTH)

root.mainloop()