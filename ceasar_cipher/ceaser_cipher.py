
#Creating the caesar cipher

import art as a


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z''a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(f'{a.logo}')


def caesar(text, shift, direction):
    if shift > 26:
        shift = shift % 25 #So if someone puts 27 it knows the letter is actually 'a' and so on

    cipher_text = ''
    if direction == 'encode':
        for letter in text: #Checks for spaces and place a space where necessary
            if letter == ' ':
                cipher_text += letter
            else:
                location = alphabet.index(letter) + shift #Checks letter against the encode cypher and places the new letter
                cipher_text += alphabet[location]
            
    elif direction == 'decode':
        for letter in text:
            if letter == ' ':
                cipher_text += letter
            else:
                location = alphabet.index(letter) - shift #This block decodes so it will reverse the shift once you have your code in place
                cipher_text += alphabet[location]
    print(cipher_text)

keep_going = True

#This will keep going while true and will ask if they want to encode or decode a message and print out the results to send or to read
while keep_going:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction.lower() == 'encode':
        caesar(text, shift, direction = 'encode')
    elif direction.lower() == 'decode':
        caesar(text, shift, direction = 'decode')
    
    again = input('Want to continue? Y/N\n')#Ask if the user want to continue or end the loop here
    if again.lower() == 'n':
        keep_going = False 
        print('Good Bye')
