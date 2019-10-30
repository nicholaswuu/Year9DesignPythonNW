#Input:

pronoun = input("Pronoun:")
verb = input("Verb:")

#Process and output:
n = len(verb) #sets n as the length of the "verb" string
pronoun = pronoun[0].upper()+pronoun[1:].lower() #sets the pronoun to have a capital first letter
verb = verb.lower() #sets all letters of the verb to be lower case, in case the user inputs it in uppercase, where the program cant read it.


if pronoun == "Je":	#Check what pronoun it is to determine how to conjugate the auxiliary
	newpronoun = "J'ai"

if pronoun == "Tu":
	newpronoun = pronoun + " as"

if pronoun == "Il" or pronoun == "Elle" or pronoun == "On":
	newpronoun = pronoun + " a"

if pronoun == "Nous":
	newpronoun = pronoun + " avons"

if pronoun == "Vous":
	newpronoun = pronoun + " avez"

if pronoun == "Ils" or pronoun == "Elles":
	newpronoun = pronoun + " ont"


if verb[n-2:n] == "er": #check if the verb is an -er verb and if the 
	print(newpronoun + " "+verb[:n-2]+"é") #if it is, output the conjugated version by taking away "er" and adding é

if verb[n-2:n] == "ir":	#check if the verb is an -ir verb
	print(newpronoun + " "+verb[:n-1]) #if it is, output the conjugated version by deleting the "r"

if verb[n-2:n] == "re":	#check if the verb is an -re verb
	print(newpronoun + " "+verb[:n-2]+"u") #if it is, output the conjugated version by taking away "re" and adding "u"