import random

def validate_letter(letter, word):
    """
    Verify if letter is in word

    param str letter a single alpha character
    param str word any word 
    returns True if letter is in word or False if not
    """
    try:
        assert letter.isalpha() == True, '▲ ONLY TRY LETTERS ▲'
        return letter.upper() in word
    except AssertionError as e:
        print(e)
        return validate_letter(input(), word)


def main():
    WORDS = ('SPACE', 'PYTHON', 'LOOK', 'CAKE', 'COOKIE', 'PLATZI')
    word = random.choice(WORDS)
    # print word, '-' instead letters
    secret_word = ['-' for i in word]
    secret_word = ''.join(secret_word)
    print(f'Guess the word: \n{secret_word}')

    # Recive letter
    letter = input('Choose a letter: ')
    is_in_word = validate_letter(letter, word)
    print(is_in_word)

# look if the letter is in the word
# print result

if __name__ == "__main__":
    print('WELCOME!!')
    main()