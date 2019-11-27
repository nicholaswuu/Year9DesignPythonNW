import tkinter as tk
import os
import random

drmrsv = ["devenir", "revenir", "monter", "rester", "sortir", "venir", "aller", "naître", "descendre", "entrer", "rentrer", "tomber", "retourner", "arriver", "mourir", "partir"]
irregular = ["atteindre", "avoir", "boire", "conduire", "connaître", "construire", "courir", "couvrir", "craindre", "croire", "devoir", "dire", "écrire", "être", "faire", "falloir", "instruire", "joindre", "lire", "mettre", "mourir", "offrir", "ouvrir", "naître", "paraître", "peindre", "pleuvoir", "pouvoir", "prendre", "produire", "recevoir", "savoir", "souffrir", "suivre", "tenir", "venir", "vivre", "voir", "vouloir", "revenir", "devenir", "naître"]
irregularnew = ["atteint", "eu", "bu", "conduit", "connu", "construit", "couru", "couvert", "craint", "cru", "dû", "dit", "écrit", "été", "fait", "fallu", "instruit", "joint", "lu", "mis", "mort", "offert", "ouvert", "né", "paru", "peint", "plu", "pu", "pris", "produit", "reçu", "su", "souffert", "suivi", "tenu", "venu", "vécu", "vu", "voulu", "revient", "devenu", "né"]
sentencends = ["un poisson.", "au café.", "à la parc.", "de la musique.", "à l'hôpital."]

def checkans(*args):
	if var.get() == "pronoun" and vari.get() == "auxiliary" and varia.get() == "past participle":
		correct.grid(row = 2, column = 3)
	else:
		incorrect.grid(row = 2, column = 3)

def conj(*args):
	pronoun = pnEntry.get()
	pnEntry.delete(0,tk.END)
	verb = verbEntry.get()
	verbEntry.delete(0,tk.END)
	n = len(verb) 
	pronoun = pronoun[0].upper()+pronoun[1:].lower() #sets the pronoun to have a capital first letter
	verb = verb.lower()
	sentenceend = random.choice(sentencends)

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

	conjtext.grid(column = 0, columnspan = 2, row = 6, pady = 10)
	conjtext.config(state = "normal")
	conjtext.delete("1.0",tk.END)
	extext.grid(column = 2, columnspan = 2, row = 6, pady = 10)
	extext.config(state = "normal")
	extext.delete("1.0",tk.END)

	def	audio():
		nonlocal newpronoun, newverb
		newpronoun = newpronoun.replace("'", "")
		newverb = newverb.replace("(e)", "")
		newverb = newverb.replace("(s)", "")
		if newverb[len(newverb)-1] == "é":
			newverb = newverb[:len(newverb)-2] + "er"
		os.system("say -v Thomas " + newpronoun + newverb)

	def audio2():
		nonlocal newpronoun, newverb, sentenceend
		newpronoun = newpronoun.replace("'", "")
		newverb = newverb.replace("(e)", "")
		newverb = newverb.replace("(s)", "")
		sentenceend = sentenceend.replace("'", "")
		if newverb[len(newverb)-1] == "é":
			newverb = newverb[:len(newverb)-2] + "er"
		os.system("say -v Thomas " + newpronoun + newverb + " " + sentenceend)

	step1 = " Step 1: Insert step 1"
	step2 = " Step 2: Insert step 2"
	result = step1 + "\n\n" + step2 + "\n\n\n" + " " + newpronoun + newverb
	example = " " + newpronoun + newverb + " " + sentenceend
	#audio buttons
	audiobtn = tk.Button(root, text = "Audio")
	audiobtn.config(command = audio, height = 2, font = ("arvo", 16), highlightbackground = "#e5f6ff")
	audiobtn.grid(row = 6, column = 0, sticky = "sw", padx = 25, pady = 30)
	audiobtn2 = tk.Button(root, text = "Audio")
	audiobtn2.config(command = audio2, height = 2, font = ("arvo", 16), highlightbackground = "#e5f6ff")
	audiobtn2.grid(row = 6, column = 2, sticky="sw", padx = 15, pady = 30)

	conjtext.insert(tk.END, result)
	conjtext.config(state = "disabled")	
	extext.insert(tk.END, example)
	extext.config(state = "disabled")

def highcontrast(*args):
	root.config(bg = "#0019a6")
	titlelabel.config(bg = "black", fg = "white")
	eq1.config(bg = "#0019a6", fg = "white")
	eq2.config(bg = "#0019a6", fg = "white")
	eq3.config(bg = "#0019a6", fg = "white")
	drop1.config(bg = "white")
	drop2.config(bg = "white")
	drop3.config(bg = "white")
	pnlabel.config(bg = "#0019a6", fg = "white")
	verblabel.config(bg = "#0019a6", fg = "white")
	textbox.config(bg = "black", fg = "white")
	conjtext.config(bg = "black", fg = "white")
	extext.config(bg = "black", fg = "white")
	highc.config(bg = "#0019a6", fg = "white")
	correct.config(bg = "#0019a6", fg = "#52ff54")
	incorrect.config(bg = "#0019a6")

#GUI	
root = tk.Tk()
root.title("French Conjugator")

optionlist=["auxiliary", "past participle", "pronoun"]
var = tk.StringVar(root)
var.set(optionlist[0])
vari = tk.StringVar(root)
vari.set(optionlist[0])
varia = tk.StringVar(root)
varia.set(optionlist[0])

frbutton = tk.Button(root, text = "Fr")
frbutton.config(font = ("arvo", 15), fg = "#003274", width = 3, height = 2)
frbutton.grid(row = 0, column = 0, sticky = "w", padx = 50)

enbutton = tk.Button(root, text = "En")
enbutton.config(font = ("arvo", 15), fg = "#003274", width = 3, height = 2)
enbutton.grid(row = 0, column = 0, sticky = "w", padx = 10)

titlelabel = tk.Label(root, text = "Passé Compose Conjugator")
titlelabel.config(width = 25, height = 2, bg = "#c5eeff", font = ("arvo bold", 25), fg = "#007691")
titlelabel.grid(columnspan = 5, pady = 15, row = 0)

eq1 = tk.Label(root, text = "Passé Compose =  ")
eq1.config(font = ("arvo", 18), bg = "#e5f6ff")
eq1.grid(row = 1, column = 0, sticky = "e")

drop1 = tk.OptionMenu(root, var, *optionlist)
drop1.config(width = 11, bg = "#e5f6ff")
drop1.grid(row = 1, column = 1, sticky = "w")

eq2 = tk.Label(root, text = "+")
eq2.config(font = ("arvo", 20), bg = "#e5f6ff")
eq2.grid(row = 1, column = 1, sticky = "e")

drop2 = tk.OptionMenu(root, vari, *optionlist)
drop2.config(width = 11, bg = "#e5f6ff")
drop2.grid(row = 1, column = 2, sticky = "w")

eq3 = tk.Label(root, text = "+")
eq3.config(font = ("arvo", 20), bg = "#e5f6ff")
eq3.grid(row = 1, column = 2, sticky = "e")

drop3 = tk.OptionMenu(root, varia, *optionlist)
drop3.config(width = 11, bg = "#e5f6ff")
drop3.grid(row = 1, column = 3, sticky = "w")

check = tk.Button(root, text = "Check Answer")
check.config(fg = "#003274", highlightbackground = "#89dbff", width = 16, height = 2, font = ("arvo", 16), command = checkans)
check.grid(column = 1, columnspan = 2, row = 2, pady = 10)

correct = tk.Label(root, text = "√ Correct!")
correct.config(fg = "green", font = ("arvo", 18), bg = "#e5f6ff")

incorrect = tk.Label(root, text = "X Incorrect!")
incorrect.config(fg = "red", font = ("arvo", 18), bg = "#e5f6ff")

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

conjtext = tk.Text(root, relief = tk.FLAT)
conjtext.config(font = ("arvo", 16), width = 28, height = 15, state = "disabled")

extext = tk.Text(root, relief = tk.FLAT)
extext.config(font = ("arvo", 16), width = 28, height = 15, state = "disabled")

highc = tk.Checkbutton(root, text = "High Contrast")	#Checkbox for high contrast
highc.config(bg = "#e5f6ff", command = highcontrast)
highc.grid(column = 3, columnspan = 2, row = 7)

root.config(bg = "#e5f6ff")
root.mainloop()