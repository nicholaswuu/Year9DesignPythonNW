import tkinter as tk

drmrsv = ["devenir", "revenir", "monter", "rester", "sortir", "venir", "aller", "naître", "descendre", "entrer", "rentrer", "tomber", "retourner", "arriver", "mourir", "partir"]
irregular = ["atteindre", "avoir", "boire", "conduire", "connaître", "construire", "courir", "couvrir", "craindre", "croire", "devoir", "dire", "écrire", "être", "faire", "falloir", "instruire", "joindre", "lire", "mettre", "mourir", "offrir", "ouvrir", "naître", "paraître", "peindre", "pleuvoir", "pouvoir", "prendre", "produire", "recevoir", "savoir", "souffrir", "suivre", "tenir", "venir", "vivre", "voir", "vouloir", "revenir", "devenir", "naître"]
irregularnew = ["atteint", "eu", "bu", "conduit", "connu", "construit", "couru", "couvert", "craint", "cru", "dû", "dit", "écrit", "été", "fait", "fallu", "instruit", "joint", "lu", "mis", "mort", "offert", "ouvert", "né", "paru", "peint", "plu", "pu", "pris", "produit", "reçu", "su", "souffert", "suivi", "tenu", "venu", "vécu", "vu", "voulu", "revient", "devenu", "né"]

def conj(*args):
	pronoun = pnEntry.get()
	pnEntry.delete(0,tk.END)
	verb = verbEntry.get()
	verbEntry.delete(0,tk.END)
	n = len(verb) 
	pronoun = pronoun[0].upper()+pronoun[1:].lower() #sets the pronoun to have a capital first letter
	verb = verb.lower()

	if verb[n-2:n] == "er" and verb not in irregular:
		newverb = verb[:n-2]+"é" 

	if verb[n-2:n] == "ir" and verb not in irregular:
		newverb = verb[:n-1]

	if verb[n-2:n] == "re" and verb not in irregular:
		newverb = verb[:n-2]+"u" 

	if verb in irregular:
		for i in range(len(irregular)):
			if verb == irregular[i]:
				newverb = irregularnew[i]

	if pronoun == "Je" and verb in drmrsv:
		newpronoun = "Je suis "
		newverb = newverb + "(e)"
	if pronoun == "Je" and verb not in drmrsv:
		newpronoun = "J'ai "

	if pronoun == "Tu" and verb in drmrsv:
		newpronoun = pronoun + " es "
		newverb = newverb + "(e)"
	if pronoun == "Tu" and verb not in drmrsv:
		newpronoun = pronoun + " as "

	if pronoun == "Il" and verb in drmrsv or pronoun == "Elle" and verb in drmrsv or pronoun == "On" and verb in drmrsv:
		newpronoun = pronoun + " est "
		if pronoun == "Elle":
			newverb = newverb + "e"
		if pronoun == "On":
			newverb = newverb + "(e)s"
	if pronoun == "Il" and verb not in drmrsv or pronoun == "Elle" and verb not in drmrsv or pronoun == "On" and verb not in drmrsv:
		newpronoun = pronoun + " a "

	if pronoun == "Nous" and verb in drmrsv:
		newpronoun = pronoun + " sommes "
		newverb = newverb + "(e)s"
	if pronoun == "Nous" and verb not in drmrsv:
		newpronoun = pronoun + " avons "

	if pronoun == "Vous" and verb in drmrsv:
		newpronoun = pronoun + " êtes "
		newverb = newverb + "(e)(s)"
	if pronoun == "Vous" and verb not in drmrsv:
		newpronoun = pronoun + " avez "

	if pronoun == "Ils" and verb in drmrsv or pronoun == "Elles" and verb in drmrsv:
		newpronoun = pronoun + " sont "
		if pronoun == "Elles":
			newverb = newverb + "es"
		if pronoun == "Ils":
			newverb = newverb + "s"
	if pronoun == "Ils" and verb not in drmrsv or pronoun == "Elles" and verb not in drmrsv:
		newpronoun = pronoun + " ont "

	conjtext.config(state = "normal")
	conjtext.delete("1.0",tk.END)
	step1 = "Step 1: Insert step 1"
	step2 = "Step 2: Insert step 2"
	result = step1 + "\n\n" + step2 + "\n\n\n" + newpronoun + newverb
	conjtext.insert(tk.END, result)
	conjtext.config(state = "disabled")

#GUI

root = tk.Tk()
root.title("Conjugator")

optionlist=["auxiliary", "past participle", "pronoun"]

frbutton = tk.Button(root, text = "French")
frbutton.config(font = ("arvo", 12), highlightbackground = "#e5f6ff")
frbutton.grid(row = 0, column = 0, sticky = "w", padx = 5)

enbutton = tk.Button(root, text = "English")
enbutton.config(font = ("arvo", 12), highlightbackground = "#e5f6ff")
enbutton.grid(row = 0, column = 0)

titlelabel = tk.Label(root, text = "Passé Compose Conjugator")
titlelabel.config(width = 25, height = 2, bg = "#c5eeff", font = ("arvo bold", 25), fg = "#007691")
titlelabel.grid(columnspan = 5, pady = 15, row = 0)

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
conjbutton.config(fg = "#003274", highlightbackground = "#89dbff", width = 15, height=2, command = conj)
conjbutton.grid(column = 3, row = 4, rowspan = 2, sticky = "w")

conjtext = tk.Text(root)
conjtext.config(font = ("arvo", 16), width = 28, height = 15, state = "disabled")
conjtext.grid(column = 0, columnspan = 2, row = 6, pady = 10)

extext = tk.Text(root)
extext.config(font = ("arvo", 16), width = 28, height = 15, state = "disabled")
extext.grid(column = 2, columnspan = 2, row = 6, pady = 10)

highc = tk.Checkbutton(root, text = "High Contrast")	#Checkbox for high contrast
highc.config(bg = "#e5f6ff")
highc.grid(column = 3, columnspan = 2)

root.config(bg = "#e5f6ff")
root.mainloop()