import os

#Input:

pronoun = input("Pronoun:")
verb = input("Verb:")
drmrsv = ["devenir", "revenir", "monter", "rester", "sortir", "venir", "aller", "naître", "descendre", "entrer", "rentrer", "tomber", "retourner", "arriver", "mourir", "partir"]
irregular = ["atteindre", "avoir", "boire", "conduire", "connaître", "construire", "courir", "couvrir", "craindre", "croire", "devoir", "dire", "écrire", "être", "faire", "falloir", "instruire", "joindre", "lire", "mettre", "mourir", "offrir", "ouvrir", "naître", "paraître", "peindre", "pleuvoir", "pouvoir", "prendre", "produire", "recevoir", "savoir", "souffrir", "suivre", "tenir", "venir", "vivre", "voir", "vouloir", "revenir", "devenir", "naître"]
irregularnew = ["atteint", "eu", "bu", "conduit", "connu", "construit", "couru", "couvert", "craint", "cru", "dû", "dit", "écrit", "été", "fait", "fallu", "instruit", "joint", "lu", "mis", "mort", "offert", "ouvert", "né", "paru", "peint", "plu", "pu", "pris", "produit", "reçu", "su", "souffert", "suivi", "tenu", "venu", "vécu", "vu", "voulu", "revient", "devenu", "né"]

#Process:
n = len(verb) #sets n as the length of the "verb" string
pronoun = pronoun[0].upper()+pronoun[1:].lower() #sets the pronoun to have a capital first letter
verb = verb.lower() #sets all letters of the verb to be lower case, in case the user inputs it in uppercase, where the program cant read it.

#Verb checking

if verb[n-2:n] == "er" and verb not in irregular:	#check if the verb is a regular -er verb
	newverb = verb[:n-2]+"é" #if it is, the conjugated verb is made taking away "er" and adding é

if verb[n-2:n] == "ir" and verb not in irregular:	#check if the verb is a regular -ir verb
	newverb = verb[:n-1]	#if it is, the conjugated verb is made taking away "r"

if verb[n-2:n] == "re" and verb not in irregular:	#check if the verb is a regular -re verb
	newverb = verb[:n-2]+"u" #if it is, the conjugated verb is made taking away "re" and adding u

if verb in irregular:
	for i in range(len(irregular)):
		if verb == irregular[i]:
			newverb = irregularnew[i]

#Pronoun checking

if pronoun == "Je" and verb in drmrsv:	#Check what pronoun it is to determine how to conjugate the auxiliary
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

#Output

print(newpronoun + newverb)

newpronoun = newpronoun.replace("'", "")	#Because the computer can't say ' or ( or )
newverb = newpronoun.replace("(", "")
newverb = newpronoun.replace(")", "")
os.system("say -v Thomas " + newpronoun + " "+ newverb)
