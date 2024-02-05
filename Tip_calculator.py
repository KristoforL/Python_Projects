#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print('Welcome to the tip calculator!')
cost = float(input("What is the bill amount?\n$"))
people = int(input("How many people are paying?\n"))
tip = float(input("What percentage tip do you want to leave? 10 15 18 20 or custom amount\n"))

#cost = float(cost)
#people = int(people)
#tip = (float(tip) * .01) + 1 #Converts it to a percentage and adds one
tip = tip * .01 + 1
with_tip = cost * tip #Added one to the tip above so that we can get the total amount with the tip

#The total bill will be the cost with tip divided by total people paying
bill = "{:.2f}".format(with_tip / people) #Used format() here so that we will always get 2 digits behind the decimal
print(f'Each person should pay ${bill}.')