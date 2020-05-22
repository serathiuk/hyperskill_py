import random
import re

words = ['python', 'java', 'kotlin', 'javascript']


def play():
    secret_word = words[random.randint(0, 3)]

    print("H A N G M A N")

    hidden_word = '-' * len(secret_word)
    letters_typed = set()

    tries = 0
    while tries < 8:
        print()
        print(hidden_word)

        letter = input("Input a letter:")

        if len(letter) != 1:
            print('You should print a single letter.')
            continue
        elif not re.match('[a-z]+', letter):
            print('It is not an ASCII lowercase letter.')
            continue
        elif letter in letters_typed:
            print('You already typed this letter .')
            continue

        letters_typed.add(letter)

        if letter in secret_word:
            aux_word = ''
            improvements = False
            for i in range(len(secret_word)):
                if letter == secret_word[i] and hidden_word[i] == '-':
                    aux_word += secret_word[i]
                    improvements = True
                else:
                    aux_word += hidden_word[i]

            hidden_word = aux_word

            if not improvements:
                print('You already typed this letter .')
        else:
            print('No such letter in the word')
            tries += 1

    print('Thanks for playing!')

    total_guessed = len(hidden_word.replace('-', ''))
    word_length = len(secret_word)
    if total_guessed == word_length:
        print("You guessed the word!")
        print("You survived!")
    else:
        print('You are hanged!')


while True:
    option = input('Type "play" to play the game, "exit" to quit:')
    if option == 'play':
        play()
    elif option == 'exit':
        break
