import auction_art as aa #This may not be the best way to shorten the name but because this is local and not for a larger project team we will stick to aa

print(f'{aa.logo}\nWelcome to the blind Auction')

adding = True
bids = {} #This is a dictionary that will have key which is the name and the value is the the bid they place

#This function will take in two parameters with the name and bid
def add_bids(name, bid):
    bids[name] = bid

#This function will deteremine who the winner of the bid is.
def winner(bids):
    winner = ''
    winning_bid = 0
    for bidder in bids: #Checks the value of the key(bidder) to see if it is greater than winning bid and if it is then winning bid will be set to that amount
        if bids[bidder] > winning_bid: 
            winner = bidder #Sets the winner to the bidder name
            winning_bid = bids[bidder] #Sets the winning bid to bidder value
    print(f'The winner of the auciton is {winner.title()} with a bid of ${winning_bid}')

    
while adding: #This will loop through until all bidders are in the system
    name = input('What is your name:\n')
    bid = int(input('What is your bid:\n$'))
    add_bids(name, bid)
    another = input('Is there another bidder? Y/N\n') #Checks if there is another bidder but if the user puts anything other than N then it will continue. Could be fixed if it was a loop that would let them know to try again with the correct entry.
    if another.lower() == 'n':
        winner(bids)
        adding = False













