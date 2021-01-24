import unittest


def validate_letter(letter, word):
    """
    Verify if letter is in word

    param str letter a single alpha character
    param str word any word 
    returns a list, first element is a bool if letter is in word, second is the letter
    """
    try:
        assert letter.isalpha() == True, '▲ ONLY TRY LETTERS ▲'
        letter = letter.upper()
        return [letter in word, letter]
    except AssertionError as e:
        print(e)
        return validate_letter(input(), word)



class BlackBox(unittest.TestCase):
    def test_dont_accept_numbers(self):
        letter = '25'
        word = 'BERLIN'
        outcome = validate_letter(letter, word)

        self.assertEqual(outcome, validate_letter(input(), word))

    def test_dont_accept_simbols(self):
        letter = '.'
        word = 'BERLIN'
        outcome = validate_letter(letter, word)

        self.assertEqual(outcome, validate_letter(input(), word))
    
    def test_dont_accept_empty_str(self):
        letter = ''
        word = 'BERLIN'
        outcome = validate_letter(letter, word)

        self.assertEqual(outcome, validate_letter(input(), word))

    def test_in_word(self):
        letter = 'N'
        word = 'BERLIN'
        outcome = validate_letter(letter, word)

        self.assertEqual(outcome, [True, letter])

    def test_not_case_sensitive(self):
        letter = 'b'
        word = 'BERLIN'
        outcome = validate_letter(letter, word)

        self.assertEqual(outcome, [True, letter.upper()])

    def test_not_in_letter(self):
        letter = 'z'
        word = 'BERLIN'
        outcome = validate_letter(letter, word)

        self.assertEqual(outcome, [False, letter.upper()])


if __name__ == "__main__":
    unittest.main()