import calculator_art as ca


print(f'{ca.logo}')

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2    

operations = {
    '+':add,
    '-':subtract, 
    '*':multiply, 
    '/':divide
}


def calculator():

    num1 = float(input('What is the first number:\n'))

    for symbol in operations:
        print(symbol)

    more_math = True
    while more_math:
        pick = input('Pick operation symbol or x to exit:\n')

        if pick.lower() == 'x':
            print('Thank you for using the calculator')
            break
        num2 = float(input('What is the second number number:\n'))

        #This is where the operation function is called
        init_answer = operations[pick](num1, num2)

        print(f'{num1} {pick} {num2} = {init_answer}')
        #There is no need for a name variable below when comparing in an if statement
        forward = input('Would you like to continue? Y/N\n').lower() 
        
        if forward == 'n': 
            print('Goodbye')
            more_math = False
            calculator()
        elif forward == 'y':
            num1 = init_answer
            print(f'{num1}\n')
            pick = input('Pick operation symbol:\n')

            num2 = float(input('What is the second number number:\n'))

            init_answer = operations[pick](num1, num2)

            print(f'{num1} {pick} {num2} = {init_answer}')
        else:
            print('Please use correct input to continue next time')

calculator()

    
