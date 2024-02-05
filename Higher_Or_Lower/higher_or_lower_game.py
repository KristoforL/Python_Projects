import game_data as ga
import random as r
import higher_or_lower_art as hla
import sys as s
import os

#Create a function that randomly selects a persons dictionary from the data list in the data file

#Create a functiont to increase the score

#Create a function to display the data in the dictionary for the player

#Create a function to compare the followers of the random people and check if user is correct

#Repeat the comparison if the user is right and if they are wrong end the program and show the score




def clear():
    """Clears the window based on the operating system"""
    if s.platform == "linux" or s.platform == "linux2":
        #linux
        os.system('clear')
    elif s.platform == "darwin":
        # OS X
        os.system("clear")
    elif s.platform == "win32":
        # Windows...
        os.system("cls")

def data():
    """Gets a random piece of data from game data file"""
    clear()
    return r.choice(ga.data)

def score_up(a):
    """Increases the score"""
    a +=1
    return a

def vs(a, b):
    """Shows who the player has to choose between"""  
    #Made it less congested and more readable
    a_formatted = f"A: {a['name']}, {a['description']} from {a['country']}"
    b_formatted = f"B: {b['name']}, {b['description']} from {b['country']}"

    print(f'{a_formatted}\n{hla.vs}\n{b_formatted}')

def high_lower():
    score = 0
    choice1 = data()
    choice2 = data()
    
    gameover = False
    
    while not gameover:
        
        print(hla.logo)

        if choice1 == choice2:
            choice2 = data()

        vs(choice1, choice2)
        
        guess = input('Does A or B have more followers? A/B\n').lower()

        if guess == 'a':
            if choice1['follower_count'] > choice2['follower_count']:
                score = score_up(score)
                choice2 = data()
                clear()
                print(f'Score: {score}\nCorrect!!')
            elif choice2['follower_count'] > choice1['follower_count']:
                clear()
                print(f'Sorry that is wrong.\nYour score: {score}')
                gameover = True
        elif guess == 'b':
            if choice2['follower_count'] > choice1['follower_count']:
                score = score_up(score)
                replace = choice2
                choice1 = replace
                choice2 = data()
                clear()
                print(f'Score: {score}\nCorrect!!')
            elif choice1['follower_count'] > choice2['follower_count']:
                clear()
                print(f'Sorry that is wrong.\nYour score: {score}')
                gameover = True
        else:
            print('Please select from A or B only.')


while input('Do you want to play higher or lower follower game? Y/N\n').lower() == 'y':
    clear()
    high_lower()
else:
    clear()
    print('Thank you')







