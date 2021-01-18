import random


def main():
    WORDS = ('SPACE', 'PYTHON', 'LOOK', 'CAKE', 'COOKIE', 'PLATZI')
    word = random.choice(WORDS)
    # print word, '-' instead letters
    secret_word = ['-' for i in word]
    secret_word = ''.join(secret_word)
    print(f'Guess the word: \n{secret_word}')

    # Recive letter
    letter = input('Choose a letter: ')
    is_in_word = validate_letter(letter)

# look if the letter is in the word
# print result

if __name__ == "__main__":
    print('WELCOME!!')
    main()