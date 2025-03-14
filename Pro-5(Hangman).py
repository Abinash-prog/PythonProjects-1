import random
import string

from Hangman.Words import words

def get_valid_word(words):
    word = random.choice(words) #Randomly choose something from the list
    while '_' in word or ''in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # What the user has guessed
    # Getting user input

    while len(word_letters) > 0:
        # letters used
        print('You have used these letters', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word:', ' '.join(word_list))



        user_letter = input('Guess a letter').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print('You have already guessed that letter, Please try again')
        
        else:
            print('Invalid charater. Please try again')

user_input = input('Type something:')


hangman()

print(user_input)



















