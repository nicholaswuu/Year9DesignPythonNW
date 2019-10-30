#Input:

pronoun = input("Pronoun:")
verb = input("Verb:")

#Process and output:
n = len(verb)

if verb[n-2:n] == "er": #check if the verb is an -er verb
	print(pronoun + " "+verb[:n-2]+"é") #if it is, output the conjugated version by taking away "er" and adding é

if verb[n-2:n] == "ir":	#check if the verb is an -ir verb
	print(pronoun + " "+verb[:n-1]) #if it is, output the conjugated version by deleting the "r"

if verb[n-2:n] == "re":	#check if the verb is an -re verb
	print(pronoun + " "+verb[:n-2]+"u") #if it is, output the conjugated version by taking away "re" and adding "u"