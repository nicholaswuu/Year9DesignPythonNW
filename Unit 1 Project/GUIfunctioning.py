import tkinter as tk
from tkinter import messagebox
import os
import random

drmrsv = ["devenir", "revenir", "monter", "rester", "sortir", "venir", "aller", "naître", "descendre", "entrer", "rentrer", "tomber", "retourner", "arriver", "mourir", "partir"]
irregular = ["atteindre", "avoir", "boire", "conduire", "connaître", "construire", "courir", "couvrir", "craindre", "croire", "devoir", "dire", "écrire", "être", "faire", "falloir", "instruire", "joindre", "lire", "mettre", "mourir", "offrir", "ouvrir", "naître", "paraître", "peindre", "pleuvoir", "pouvoir", "prendre", "produire", "recevoir", "savoir", "souffrir", "suivre", "tenir", "venir", "vivre", "voir", "vouloir", "revenir", "devenir", "naître"]
irregularnew = ["atteint", "eu", "bu", "conduit", "connu", "construit", "couru", "couvert", "craint", "cru", "dû", "dit", "écrit", "été", "fait", "fallu", "instruit", "joint", "lu", "mis", "mort", "offert", "ouvert", "né", "paru", "peint", "plu", "pu", "pris", "produit", "reçu", "su", "souffert", "suivi", "tenu", "venu", "vécu", "vu", "voulu", "revient", "devenu", "né"]
sentencends = ["un poisson.", "au café.", "à la parc.", "de la musique.", "à l'hôpital."]

print("Start Program")
file = open("data.txt", "w")
#Functions

def on_closing():
	print("Closing")
	if messagebox.askokcancel("Quit", "Do you want to quit?"):
		root.destroy()

def checkans(*args):
	if var.get() == "pronoun" and vari.get() == "auxiliary" and varia.get() == "past participle":
		correct.grid(row = 2, column = 3)
		incorrect.grid_remove()
	else:
		incorrect.grid(row = 2, column = 3)
		correct.grid_remove()

def conj(*args):
	pronoun = pnEntry.get()
	verb = verbEntry.get()
	n = len(verb) 
	pnEntry.delete(0,tk.END)
	verbEntry.delete(0,tk.END)
	pronoun = pronoun[0].upper()+pronoun[1:].lower() #sets the pronoun to have a capital first letter
	verb = verb.lower()
	sentenceend = random.choice(sentencends)
	file.write("Pronoun: " + pronoun + "\nVerb: " + verb)

	textbox.grid_remove()


	if verb[n-2:n] == "er" and verb not in irregular:
		ending = "é"
		newverb = verb[:n-2] + ending 

	if verb[n-2:n] == "ir" and verb not in irregular:
		ending = "i"
		newverb = verb[:n-2] + ending 

	if verb[n-2:n] == "re" and verb not in irregular:
		ending = "u"
		newverb = verb[:n-2] + ending 

	if verb in irregular:
		for i in range(len(irregular)):
			if verb == irregular[i]:
				newverb = irregularnew[i]

	if pronoun == "Je" and verb in drmrsv:
		aux = " suis "
		newpronoun = pronoun + aux
		newerverb = newverb + "(e)"
	if pronoun == "Je" and verb not in drmrsv:
		aux = "ai "
		newpronoun = "J'" + aux

	if pronoun == "Tu" and verb in drmrsv:
		aux = " es "
		newpronoun = pronoun + aux
		newerverb = newverb + "(e)"
	if pronoun == "Tu" and verb not in drmrsv:
		aux = " as "
		newpronoun = pronoun + aux

	if pronoun == "Il" and verb in drmrsv or pronoun == "Elle" and verb in drmrsv or pronoun == "On" and verb in drmrsv:
		aux = " est "
		newpronoun = pronoun + aux
		if pronoun == "Elle":
			newerverb = newverb + "e"
		if pronoun == "On":
			newerverb = newverb + "(e)s"
	if pronoun == "Il" and verb not in drmrsv or pronoun == "Elle" and verb not in drmrsv or pronoun == "On" and verb not in drmrsv:
		aux = " a "
		newpronoun = pronoun + aux

	if pronoun == "Nous" and verb in drmrsv:
		aux = " sommes "
		newpronoun = pronoun + aux
		newerverb = newverb + "(e)s"
	if pronoun == "Nous" and verb not in drmrsv:
		aux = " avons "
		newpronoun = pronoun + aux

	if pronoun == "Vous" and verb in drmrsv:
		aux = " êtes "
		newpronoun = pronoun + aux
		newerverb = newverb + "(e)(s)"
	if pronoun == "Vous" and verb not in drmrsv:
		aux = " avez "
		newpronoun = pronoun + aux

	if pronoun == "Ils" and verb in drmrsv or pronoun == "Elles" and verb in drmrsv:
		aux = " sont "
		newpronoun = pronoun + aux
		if pronoun == "Elles":
			newerverb = newverb + "es"
		if pronoun == "Ils":
			newerverb = newverb + "s"
	if pronoun == "Ils" and verb not in drmrsv or pronoun == "Elles" and verb not in drmrsv:
		aux = " ont "
		newpronoun = pronoun + aux

	steptext.grid(column = 0, columnspan = 2, row = 6, rowspan = 2, padx = 5, pady = 10)
	steptext.config(state = "normal")
	steptext.delete("1.0",tk.END)
	conjtext.grid(column = 2, columnspan = 3, row = 6, padx = 5, pady = 1)
	conjtext.config(state = "normal")
	conjtext.delete("1.0",tk.END)
	extext.grid(column = 2, columnspan = 3, row = 7, padx = 5, pady = 1)
	extext.config(state = "normal")
	extext.delete("1.0",tk.END)
	file.write("\n\n" + newpronoun + newverb + "\n---\n")

	def	audio():
		nonlocal newpronoun, newerverb, newverb
		newpronoun = newpronoun.replace("'", "")
		if verb in drmrsv:
			newerverb = newerverb.replace("(e)", "")
			newerverb = newerverb.replace("(s)", "")
			if newerverb[len(newerverb)-1] == "é":
				newerverb = newerverb[:len(newerverb)-1] + "er"
			os.system("say -v Thomas " + newpronoun + newerverb)

		if verb not in drmrsv:
			if newverb[len(newverb)-1] == "é":
				newverb = newverb[:len(newverb)-1] + "er"
			os.system("say -v Thomas " + newpronoun + newverb)

	def audio2():
		nonlocal newpronoun, newerverb, newverb, sentenceend
		newpronoun = newpronoun.replace("'", "")
		if verb in drmrsv:
			newerverb = newerverb.replace("(e)", "")
			newerverb = newerverb.replace("(s)", "")
			sentenceend = sentenceend.replace("'", "")
			if newerverb[len(newerverb)-1] == "é":
				newerverb = newerverb[:len(newerverb)-1] + "er"
			os.system("say -v Thomas " + newpronoun + newerverb + " " + sentenceend)

		if verb not in drmrsv:
			sentenceend = sentenceend.replace("'", "")
			if newverb[len(newverb)-1] == "é":
				newverb = newverb[:len(newverb)-1] + "er"
			os.system("say -v Thomas " + newpronoun + newverb + " " + sentenceend)



	#Step by step explaination
	if verb in drmrsv and verb not in irregular:
		step1 = " 1. Auxiliary.\n\n    Verb = " + verb + "\n    DRMRSVANDERTRAMP verb, auxiliary is être.\n\n    Conjugate être: \n    Pronoun = " + pronoun + "\n    Conjugate: être –––>" + aux + "\n    So final auxiliary = " + aux
		step2 = " 2. Past participle.\n\n    Verb = " + verb + "\n    -" + verb[n-2:n] + " verb, replace with " + ending + "\n    Auxiliary is être, verb needs to AGREE with\n    GENDER of PRONOUN \n    Add (e) or (s) if pronoun is feminine or plural\n    Final past participle: " + newerverb
		result =  "HOW TO CONJUGATE: \n\n" + step1 + "\n\n" + step2
		answer = "ANSWER: \n\n"+ newpronoun + newerverb
		example = "EXAMPLE: \n\n " + newpronoun + newerverb + " " + sentenceend
	if verb in drmrsv and verb in irregular:
		step1 = " 1. Auxiliary.\n\n    Verb = " + verb + "\n    DRMRSVANDERTRAMP verb, auxiliary is être.\n\n    Conjugate être: \n    Pronoun = " + pronoun + "\n    Conjugate: être –––>" + aux + "\n    So final auxiliary = " + aux
		step2 = " 2. Past participle.\n\n    Verb = " + verb + "\n    Irregular verb, conjugation: " + verb + "––" + newverb + "\n    Auxiliary is être, verb needs to AGREE with\n    GENDER of PRONOUN \n    Add (e) or (s) if pronoun is feminine or plural\n    Final past participle: " + newerverb
		result =  "HOW TO CONJUGATE: \n\n" + step1 + "\n\n" + step2
		answer = "ANSWER: \n\n"+ newpronoun + newerverb
		example = "EXAMPLE: \n\n " + newpronoun + newerverb + " " + sentenceend
	if verb not in drmrsv and verb not in irregular:
		step1 = " 1. Auxiliary.\n\n    Verb = " + verb + "\n    avoir verb, auxiliary is avoir.\n\n    Conjugate avoir: \n    Pronoun = " + pronoun + "\n    Conjugate: avoir –––>" + aux + "\n    So final auxiliary = " + aux
		step2 = " 2. Past participle.\n\n    Verb = " + verb + "\n    Irregular verb, conjugation: " + verb + "––" + newverb + "\n    Auxiliary is avoir, verb doesn't need to AGREE\n    with GENDER of PRONOUN \n    Final past participle: " + newverb
		result =  "HOW TO CONJUGATE: \n\n" + step1 + "\n\n" + step2
		answer = "ANSWER: \n\n"+ newpronoun + newverb
		example = "EXAMPLE: \n\n " + newpronoun + newverb + " " + sentenceend
	if verb not in drmrsv and verb in irregular:
		step1 = " 1. Auxiliary.\n\n    Verb = " + verb + "\n    avoir verb, auxiliary is avoir.\n\n    Conjugate avoir: \n    Pronoun = " + pronoun + "\n    Conjugate: avoir –––>" + aux + "\n    So final auxiliary = " + aux
		step2 = " 2. Past participle.\n\n    Verb = " + verb + "\n    Irregular verb, conjugation: " + verb + "––" + newverb + "\n    Auxiliary is avoir, verb doesn't need to AGREE\n    with GENDER of PRONOUN \n    Final past participle: " + newverb
		result = "HOW TO CONJUGATE: \n\n"+step1 + "\n\n" + step2
		answer = "ANSWER: \n\n"+ newpronoun + newverb
		example = "EXAMPLE: \n\n " + newpronoun + newverb + " " + sentenceend

	#audio buttons
	audiobtn = tk.Button(root, text = "Audio")
	audiobtn.config(command = audio, height = 2, font = ("arvo", 16), highlightbackground = "#e5f6ff")
	audiobtn.grid(row = 6, column = 3, sticky = "se", padx = 15, pady = 20)
	audiobtn2 = tk.Button(root, text = "Audio")
	audiobtn2.config(command = audio2, height = 2, font = ("arvo", 16), highlightbackground = "#e5f6ff")
	audiobtn2.grid(row = 7, column = 3, sticky="se", padx = 15, pady = 20)

	steptext.insert(tk.END, result)
	steptext.config(state = "disabled")	
	conjtext.insert(tk.END, answer)
	conjtext.config(state = "disabled")	
	extext.insert(tk.END, example)
	extext.config(state = "disabled")

def highcontrast(*args):
	if highcon.get()==1:
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
		steptext.config(bg = "black", fg = "white")
		conjtext.config(bg = "black", fg = "white")
		extext.config(bg = "black", fg = "white")
		highc.config(bg = "#0019a6", fg = "white")
		correct.config(bg = "#0019a6", fg = "#52ff54")
		incorrect.config(bg = "#0019a6")
	if highcon.get()==0:
		root.config(bg = "#e5f6ff")
		titlelabel.config(bg = "#c5eeff", fg = "#007691")
		eq1.config(bg = "#e5f6ff", fg = "black")
		eq2.config(bg = "#e5f6ff", fg = "black")
		eq3.config(bg = "#e5f6ff", fg = "black")
		drop1.config(bg = "#e5f6ff")
		drop2.config(bg = "#e5f6ff")
		drop3.config(bg = "#e5f6ff")
		pnlabel.config(bg = "#e5f6ff", fg = "#005274")
		verblabel.config(bg = "#e5f6ff", fg = "#005274")
		textbox.config(bg = "#cff1ff", fg = "black")
		steptext.config(bg = "white", fg = "black")
		conjtext.config(bg = "white", fg = "black")
		extext.config(bg = "white", fg = "black")
		highc.config(bg = "#e5f6ff", fg = "black")
		correct.config(fg = "green", bg = "#e5f6ff")
		incorrect.config(fg = "red", bg = "#e5f6ff")

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

highcon = tk.IntVar()

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

textbox = tk.Text(root)	
textbox.config(width = 62, height = 9, state = "normal", bg = "#cff1ff", font = ("arvo", 15))
textbox.grid(row = 3, columnspan = 5, padx = 10, ipadx = 20)	
textbox.insert(tk.END, "- Passé composé is the most common past tense in French. It requires a pronoun,  auxilliary, \nand past participle. \n- The auxiliary (either avoir or être) is chosen depending on the past participle. \n- If the verb is a DRMRSVANDERTRAMP verb,  the auxiliary would be être,  otherwise,  it would \nbe avoir. \n- A past participle is the verb but in past tense,  and it's ending is changed depending on if it is \nan -er, -ir, or -re verb.\n- If the verb is a DRMRSVANDERTRAMP verb,  the past participle needs to agree with the \npronoun.")
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

conjbutton = tk.Button(root, text = "Conjugate")
conjbutton.config(fg = "#003274", highlightbackground = "#89dbff", width = 15, height=2, command = conj)
conjbutton.grid(column = 3, row = 4, rowspan = 2, sticky = "w")

steptext = tk.Text(root, relief = tk.FLAT)
steptext.config(font = ("arvo", 14), width = 33, height = 20, state = "disabled")

conjtext = tk.Text(root, relief = tk.FLAT)
conjtext.config(font = ("arvo", 16), width = 30, height = 8, state = "disabled")

extext = tk.Text(root, relief = tk.FLAT)
extext.config(font = ("arvo", 16), width = 30, height = 8, state = "disabled")

highc = tk.Checkbutton(root, text = "High Contrast")	#Checkbox for high contrast
highc.config(bg = "#e5f6ff", command = highcontrast, var = highcon, onvalue = 1, offvalue = 0)
highc.grid(column = 3, columnspan = 2, row = 8)

root.config(bg = "#e5f6ff", height = 1000)
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
file.close()
print("End Program")