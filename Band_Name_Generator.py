#This program will create a random band name with help for the user. Just have to follow the instructions in comments below:


#1. Create a greeting for your program.
print('Welcome to Band Name Generator where we will help you generate a band name!!')

#2. Ask the user for the city that they grew up in.
city = input('What city did you grow up in:\n')

#3. Ask the user for the name of a pet.
pet = input('What is the name of your pet, or what would you name your pet:\n')

#4. Ask the user for an action word or verb
action = input("What is an action word you like:\n")

#4. Combine the name of their city and pet and show them their band name.
bandname = city + ' ' + pet + ' ' + action
print('Your bandname is ' + bandname + '\n')
#5. Make sure the input cursor shows on a new line with the new line function at the end of the final output