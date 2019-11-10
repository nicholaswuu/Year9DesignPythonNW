import tkinter as tk

root = tk.Tk()
root.title("Conjugator")

optionlist=["auxiliary", "past participle", "pronoun"]

titlelabel = tk.Label(root, text = "Passé Compose Conjugator")
titlelabel.config(width = 25, height = 2, bg = "#c5eeff", font = ("arvo bold", 25), fg = "#007691")
titlelabel.grid(columnspan = 5, pady = 15)

eq1 = tk.Label(root, text = "Passé Compose =  ")
eq1.config(font = ("arvo", 18), bg = "#e5f6ff")
eq1.grid(row = 1, column = 0, sticky = "e")

drop1 = tk.OptionMenu(root, *optionlist)
drop1.config(width = 15)
drop1.grid(row = 1, column = 1, sticky = "w")

eq1 = tk.Label(root, text = "+")
eq1.config(font = ("arvo", 20), bg = "#e5f6ff")
eq1.grid(row = 1, column = 1, sticky = "e")

drop2 = tk.OptionMenu(root, *optionlist)
drop2.config(width = 15)
drop2.grid(row = 1, column = 2, sticky = "w")

eq1 = tk.Label(root, text = "+")
eq1.config(font = ("arvo", 20), bg = "#e5f6ff")
eq1.grid(row = 1, column = 2, sticky = "e")

drop3 = tk.OptionMenu(root, *optionlist)
drop3.config(width = 15)
drop3.grid(row = 1, column = 3, sticky = "w")

check = tk.Button(root, text = "Check Answer")
check.config(fg = "#003274", highlightbackground = "#89dbff", width = 16, height = 2, font = ("arvo", 16))
check.grid(column = 1, columnspan = 2, row = 2, pady = 10)

textbox = tk.Text(root)		#Textbox to place outputs and examples.
textbox.config(width = 60, height = 5, state = "normal", bg = "#cff1ff", font = ("arvo", 16))
textbox.grid(row = 3, columnspan = 5, padx = 10)	
textbox.insert(tk.END, "Explaination...")
textbox.config(state = "disabled")

pnlabel = tk.Label(root, text = "Pronoun: ")
pnlabel.config(font = ("arvo", 18), bg = "#e5f6ff", fg = "#005274")
pnlabel.grid(column = 0, row = 4, sticky = "e", pady = 10)

pnEntry = tk.Entry(root)	#Entry box will be used for pronoun
pnEntry.config(width = 30)
pnEntry.grid(column = 1, row = 4, sticky = "w", columnspan = 2)

verblabel = tk.Label(root, text = "Verb: ")
verblabel.config(font = ("arvo", 18), bg = "#e5f6ff", fg = "#005274")
verblabel.grid(column = 0, row = 5, sticky = "e")

verbEntry = tk.Entry(root)	#Entry box will be used for verb
verbEntry.config(width = 30)
verbEntry.grid(column = 1, row = 5, sticky = "w", columnspan = 2)

conjbutton = tk.Button(root, text = "Conjugate")	#Button, will be used to do the conjugation, and for audio
conjbutton.config(fg = "#003274", highlightbackground = "#89dbff", width = 15, height=2)
conjbutton.grid(column = 3, row = 4, rowspan = 2, sticky = "w")

conjtext = tk.Text(root)
conjtext.config(font = ("arvo", 14), width = 30, height = 15, state = "disabled")
conjtext.grid(column = 0, columnspan = 2, row = 6, pady = 10)

extext = tk.Text(root)
extext.config(font = ("arvo", 14), width = 30, height = 15, state = "disabled")
extext.grid(column = 2, columnspan = 2, row = 6, pady = 10)

check = tk.Checkbutton(root, text = "High Contrast")	#Checkbox for high contrast
check.config(bg = "#e5f6ff")
check.grid(column = 3, columnspan = 2)

root.config(bg = "#e5f6ff")
root.mainloop()
