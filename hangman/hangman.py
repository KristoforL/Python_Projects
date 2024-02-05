import random as r
import hangman_art as ha
import hangman_words as hw


print(f'Welcome to\n{ha.logo}')

lives = 6

chosen_word = r.choice(hw.word_list)

completed = []
for letter in chosen_word:
    completed.append('_')

print(ha.stages[lives])
print(completed)



end_game = False

while not end_game:
    guess = input('Guess a letter\n').lower()

    if guess in completed:
        print(f'You already guessed {guess}')

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            #print(guess)
            #completed.append('_')
            completed[position] = letter

    if guess not in chosen_word:
        print(f'{guess} is not in word')
        lives -= 1
        if lives == 0:
            print('You Lose')
            end_game = True
        
    
    print(completed)
    print(ha.stages[lives])

    if '_' not in completed:
        print('The word is ' + ''.join(completed) + '. You Win')
        end_game = True