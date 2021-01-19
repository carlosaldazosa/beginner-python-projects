import random

def option():
    """
    Control of times to play

    no param
    returns True to play again and False if not.
    """
    try:
        options = input('WANNA PLAY AGAIN? \n1. YES \n2. NO\n')

        assert options.isnumeric(), '▲ SELCT A VALID OPTION ▲'
        assert options == '1' or options == '2', '▲ SELCT A VALID OPTION ▲'
        if options == '1':
            return True
        else:
            print('See you next time!!')
            return False
    except:
        return option


def validate_letter(letter, word):
    """
    Verify if letter is in word

    param str letter a single alpha character
    param str word any word 
    returns True if letter is in word or False if not
    """
    try:
        assert letter.isalpha() == True, '▲ ONLY TRY LETTERS ▲'
        letter = letter.upper()
        return [letter in word, letter]
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

    # lives system
    lives = 3

    while secret_word != word:
        print(f'Lives: {lives}')

        # Recive letter
        letter = input('Choose a letter: ')
        letter = letter.upper()
        
        # Case if input is equal to word, WIN
        if letter == word:
            break

        # look if the letter is in the word
        is_in_word, letter = validate_letter(letter, word)
        print(is_in_word, letter)

        # Add letter in secret_word
        if is_in_word:
            secret_word = add_letter(word, letter, secret_word)
        else:
            lives -= 1
        
        if lives == 0:
            break
        
        # print result
        print(secret_word)

    # WIN or Loose message
    if lives != 0:
        print(f'YOU WIN!! \nThe word is {word}')
    else:
        print('YOU LOOSE\nRunned out of lives')
    


if __name__ == "__main__":
    print('WELCOME!!')
    play_again = True
    while play_again == True:
        main()
    
        play_again = option()