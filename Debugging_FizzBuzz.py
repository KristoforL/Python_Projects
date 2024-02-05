#The final project will be debugging FizzBuzz
#The below code contains bugs and is commented out because of them

# for number in range(1, 101):
#   if number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print([number])


#What I saw in the terminal was the code would print the number and fizz, buzz, or fizzbuzz. To fix that I had to make the statement an if elif else statement so that the conditions would be met and print only what was needed

#After looking into this further I see that FizzBuzz was being printed for every number divisible by 3 or 5 and not 3 and 5. so I had to change the or in the condition to and I believe this resolved all bugs in fizzbuzz

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)