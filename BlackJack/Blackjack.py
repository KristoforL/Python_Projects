#Official blackjack
import random as r
import blackjack_art as ba
import math as m
from sys import platform
import os

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


def deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] 
    return r.choice(cards)

def score(hand):
    """Calculates the scores for the players"""
    if sum(hand) == 21 and len(hand) == 2:
        return 0

    if sum(hand) > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)

    return sum(hand)

def compare(user, computer):
    """Compares scores to see who wins"""
    if user > 21 and computer > 21:
        print(f'You went over. You lose.')
    elif user == computer:
        print(f'It is a draw.')
    elif computer == 0:
        print(f'Dealer has blackjack!')
    elif user == 0:
        print(f'Player has blackjack!!')
    elif user > 21:
        print(f'Player bust! Player loses.')
    elif computer > 21:
        print(f'Dealer bust! Dealer loses.')
    elif computer > user:
        print(f'Dealer Wins!')
    elif user > computer:
        print(f'Player wins!!')

def play_game():
    print(f'{ba.logo}')

    player = []
    dealer = []

    for count in range(2):
        player.append(deal())
        dealer.append(deal())
    
    gameover = False

    while not gameover:
        player_score = score(player)
        dealer_score = score(dealer)
        print(f'Player Hand: {player} Score: {player_score}\nDealer Hand: {dealer[0]}')

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            gameover = True 
        else:
            hit = input('Do you want another card? Y/N\n').lower()
            if hit == 'y':
                player.append(deal())
                player_score = score(player)
            elif hit == 'n':
                gameover = True

    while dealer_score != 0 and dealer_score < 17:
        dealer.append(deal())
        dealer_score = score(dealer)

    compare(player_score, dealer_score)  
    print(f'Player Hand: {player} Score: {player_score}\nDealer Hand: {dealer} Score: {dealer_score}')

def clear():
    if platform == "linux" or platform == "linux2":
        #linux
        os.system('clear')
    elif platform == "darwin":
        # OS X
        os.system("clear")
    elif platform == "win32":
        # Windows...
        os.system("cls")


while input('Do you want to play blackjack? Y/N\n').lower() == 'y':
    clear()
    play_game()


clear()
print('Thank you for playing')

