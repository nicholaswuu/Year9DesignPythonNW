import tkinter as tk

root = tk.Tk()

titlelabel = tk.Label(root, text = "Passé Compose Conjugator")
titlelabel.config(width = 50, height = 2, bg = "#c5eeff", font = ("arvo", 25), fg = "#006691")
titlelabel.pack()

textbox = tk.Text(root)		#Textbox to place outputs and examples.
textbox.config(width = 100, height = 5)	
textbox.pack()
textbox.insert(tk.END, "Explaination")

pnEntry = tk.Entry(root)	#Entry box will be used for pronoun
pnEntry.config(width = 50)
pnEntry.pack()

verbEntry = tk.Entry(root)	#Entry box will be used for verb
verbEntry.config(width = 50)
verbEntry.pack()

button = tk.Button(root, text = "Conjugate")	#Button, will be used to do the conjugation, and for audio
button.config(fg = "green", width = 25, height=2)
button.pack(pady=30)

check = tk.Checkbutton(root, text = "High Contrast")	#Checkbox for high contrast
check.config(anchor = tk.W)
check.pack(fill = tk.BOTH)

root.config(bg = "#e5f6ff")
root.mainloop()
