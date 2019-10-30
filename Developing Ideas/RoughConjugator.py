#Input:

pronoun = input("Pronoun:")
verb = input("Verb:")

#Process and output:
n = len(verb)


if pronoun == "je" or "Je":	#Check what pronoun it is to determine how to conjugate the auxiliary
	newpronoun = "J'ai"
if pronoun == "tu":
	newpronoun =  pronoun + " as"
if pronoun == "il" or pronoun == "elle" or pronoun == "on":
	newpronoun = pronoun + " a"
if pronoun == "nous":
	newpronoun = pronoun + " avons"
if pronoun == "vous":
	newpronoun = pronoun + " avez"
if pronoun == "ils" or pronoun =="elles":
	newpronoun = pronoun + " ont"

if verb[n-2:n] == "er": #check if the verb is an -er verb and if the 
	print(newpronoun + " "+verb[:n-2]+"é") #if it is, output the conjugated version by taking away "er" and adding é

if verb[n-2:n] == "ir":	#check if the verb is an -ir verb
	print(newpronoun + " "+verb[:n-1]) #if it is, output the conjugated version by deleting the "r"

if verb[n-2:n] == "re":	#check if the verb is an -re verb
	print(newpronoun + " "+verb[:n-2]+"u") #if it is, output the conjugated version by taking away "re" and adding "u"