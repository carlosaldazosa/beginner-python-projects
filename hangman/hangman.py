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
        return letter in word
    except AssertionError as e:
        print(e)
        return validate_letter(input(), word)
    

def add_letter(word, letter, secret_word):
    """
    add the letter in the in secret_word

    param str word random word of the game
    param str letter single character
    param srt secret_word hide word with '-'
    returns secret_word with the letter added
    """
    word = list(word)
    secret_word = list(secret_word)
    counter = 0
    for i in word:
        if letter == i:
            secret_word[counter] = letter
        counter += 1
    secret_word = ''.join(secret_word)
    return secret_word


def main():
    words = ('SPACE', 'PYTHON', 'LOOK', 'CAKE', 'COOKIE', 'PLATZI')
    word = random.choice(words)
    # print word, '-' instead letters
    secret_word = ['-' for i in word]
    secret_word = ''.join(secret_word)
    print(f'Guess the word: \n{secret_word}')

    while secret_word != word:
        # Recive letter
        letter = input('Choose a letter: ')
        letter = letter.upper()
        
        # look if the letter is in the word
        is_in_word = validate_letter(letter, word)

        # Add letter in secret_word
        if is_in_word:
            secret_word = add_letter(word, letter, secret_word)
        
        # print result
        print(secret_word)
    


if __name__ == "__main__":
    print('WELCOME!!')
    main()