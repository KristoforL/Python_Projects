import random as r
import guessing_game_art as gga
import sys as s
import os

number = 0
guess = 0

#This is the the function that starts the game checks the level the player wants to play. This functions also checks the guess against the answer and lets the player know if they are right or not and adjust how many guesses they have left
def guess_game():
    """Play a guessing game to guess number with easy or hard modes"""

    level = input('Do you want to play easy or hard? E/H\n').lower()

    if level == 'e':
        guess = 10
    elif level == 'h':
        guess = 5
    
    while guess > 0:
        attempt = int(input('Guess a number:\n'))
        
        if attempt == number:
            print(f'{attempt} is correct! You win')
            guess = 0
        elif attempt > number:
            guess -= 1
            print(f'{attempt} is too big. You have {guess} tries left')
        else:
            guess -= 1
            print(f'{attempt} is too small You have {guess} tries left')

        if guess == 0 and attempt != number:
            print(f'Nice try but the number was {number}')


#This function checks the OS the user is on and then clears the console so if you are coding this will not be an eye sore or you dont have to clear it yourself. 
def clear():
    if s.platform == "linux" or s.platform == "linux2":
        #linux
        os.system('clear')
    elif s.platform == "darwin":
        # OS X
        os.system("clear")
    elif s.platform == "win32":
        # Windows...
        os.system("cls")


#This is a loop that will run until the user puts in anything other than y for the their answer. 
#It will ask if the player want to play, clear the console, print the logo, generate a random number, and then start the game with the guess_game function.
while input('Do you want to play a number guessing game? Y/N\n').lower() == 'y':
    clear()
    print(gga.logo)
    number = r.randint(1, 100)
    guess_game()

#Once the user enters anything other than y for the while loop above then the game will end, the console will clear, and we will thank the player for playing
clear()
print(f'Thank you. See you again')
