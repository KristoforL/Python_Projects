#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input(f"How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level - Order not randomized:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
pw = ''
for number in range(0, nr_letters):
    pw = pw + random.choice(letters)
for number in range(0, nr_symbols):
    pw = pw + random.choice(symbols)
for number in range(0, nr_numbers):
    pw = pw + random.choice(numbers)
print(pw)

#Hard Level - Order of characters randomized:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#Creates the emptypassword string 
pw = ''
#Randomly selects the number of letters, symbols, and numbers you want in your password and appends it to the password
for number in range(0, nr_letters):
    pw = pw + random.choice(letters)
for number in range(0, nr_symbols):
    pw= pw + random.choice(symbols)
for number in range(0, nr_numbers):
    pw = pw + random.choice(numbers)

#Cast the string to a list to separate the characters
pw = list(pw)
print(pw)
#Shuffle is a built in method for list where it shuffles the list so it is now random
random.shuffle(pw)
print(pw)
#Joins the list so it is one string. There is nothing between the quotes because that is what you want inserted between each string in the list. In this case we do not want any spaces between strings so that the password does not have spaces orr an unwanted characters
rpw = ''.join(pw)

print(rpw)