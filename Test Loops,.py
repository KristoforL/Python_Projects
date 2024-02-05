#In this testing file we will play around with loops and variable to create our own functions to do something.


#This program will contionue until the user does not want to continue anymore. We will make it simple for now and it will check if the number is even or not then check if the user wants to continue

go = True

def isEven():
    
    #This needs to be set to global because if it is not set inside the function it will not be changed outside the function because of the scope
    global go
    
    #This part of the code will ask for the number from the user and if return if the number is even or not. Then it will ask if the user wants to continue before setting the go boolean to false
    number = input(f"Please enter a whole number:\n")
    number = int(number)   #Cast the input to an int so that is can be checked following functions 
    if number % 2 == 0:
        print(f"{number} is even!!")
        
        #Checks that the user wants to continue and sets boolean to false if they do not want to continue
        goOn = input(f"Do you want to continue? Y/N:\n")
        if goOn.lower() == 'n':
            go = False
    else:
        print(f"{number} is NOT even!!")
        
        goOn = input(f"Do you want to continue? Y/N:\n")
        if goOn.lower() == 'n':
            go = False
        
    
#Technically this is the beginning of the code tha the user will see and begin  the interaction

##CODE STARTS HERE##
# print('Welcome to the is even function where you give me a number and I let you know if it is even')

# while go:
#     isEven()
    
# print('Thanks for playing!!')



###--------------------------------------------------------------------------###

#This is another function that will take in a users input as a parameter then count up and print every number up until the number they use

#This will simply print the numbers up to the number the user select but because the range doesn't include the last number we have to add 1 just so we can include it
def countEm(number):
    number = int(number)
    for count in range(1, number+1):
        print(count)
        
##CODE STARTS HERE##
# print('Welcome to the counter machine!!')
# number = input(f"Please input a number for me to count to:\n")

# countEm(number)


###--------------------------------------------------------------------------###

#This will be a lap calculator where it will calculate how many laps you will have to complete to have run a mile

#This function will take in one variable that will be the in or outdoor boolean. If it is true then it will calculate how many laps for an outdoor track will equal the number of miles the user puts in
def running(inOut, miles):
    miles = int(miles) #Casting the number to integer for further use
    
    #Checks the users answer for if this is an indoor or outdoor track so that the math is accurate
    if inOut.lower() == 'y':
        laps = miles * 8
        meters = miles * 1600 
        
        #Checks how many laps they are doing and lets them know if they will be running a while.
        if miles > 2:
            print(f"You will be running {laps} laps to complete {miles} miles. You are going to be running for a minute XD!!\n{meters} meters")
        else:
            print(f"You will be running {laps} laps to complete {miles} miles.")
            
        
    elif inOut.lower() == 'n':
        laps = miles * 4
        meters = miles * 1600
        
        if miles > 2:
            print(f"You will be running {laps} laps to complete {miles} miles. You are going to be running for a minute XD!!\n{meters} meters")
        else:
            print(f"You will be running {laps} laps to complete {miles} miles.")
    
    #Checks and lets them know if they did not put in an appropriate answer they will have to try again.         
    else:
        print('Please use an acceptable entry to move foward next time.')
        
        
        

##CODE STARTS HERE##
# print(f"Welcome to the mile calculator!!!\nWe will find out how many laps are needed for you to complete the number of miles you want to complete")

# miles = input(f'How many whole miles are you trying to run:\n')
# inOut = input(f'Are you running on an indoor track? Y/N:\n')

# running(inOut, miles)

    