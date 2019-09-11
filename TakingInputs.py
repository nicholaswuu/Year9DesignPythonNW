#comments are made with a #
#It is essential you comment code

#This program will take two integers 
#and multiply them

#Input
#The input function returns the string the user entered
#All inputs start as strings
#To change the type of variable you "cast" it
#Casting is the process of changing type
name = input ('Please input your name: ')
a = input ('Please input first number: ')
a = int(a)
b = input ('Please input second number: ')
b = int(b)
#Process
#What is process
product = a * b
#Output
print ('Hi, '+ name)
print ('The product of '+str(a)+' and '+str(b)+' is '+str(product)+'.')