import unittest

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

class BlackBox(unittest.TestCase):
    def test_one_time_letter(self):
        word = 'PLATZI'
        letter = 'A'
        secret_word = '------'
        outcome = add_letter(word, letter, secret_word)

        self.assertEqual(outcome, '--A---')

    def test_two_times_letter(self):
        word = 'PERRO'
        letter = 'R'
        secret_word = '-----'
        outcome = add_letter(word, letter, secret_word)

        self.assertEqual(outcome, '--RR-')

    def test_multiple_times_letter(self):
        word = 'PARALELEPIPEDO'
        letter = 'E'
        secret_word = '--------------'
        outcome = add_letter(word, letter, secret_word)

        self.assertEqual(outcome, '-----E-E---E--')



if __name__ == "__main__":
    unittest.main()