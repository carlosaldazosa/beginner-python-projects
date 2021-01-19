import unittest


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



class BlackBox(unittest.TestCase):
    def test_dont_accept_numbers(self):
        letter = '25'
        word = 'BERLIN'
        outcome = validate_letter(letter, word)

        self.assertEqual(outcome, word)

    def test_dont_accept_simbols(self):
        letter = '.'
        word = 'BERLIN'
        outcome = validate_letter(letter, word)

        self.assertEqual(outcome, word)
    
    def test_dont_accept_empty_str(self):
        letter = ''
        word = 'BERLIN'
        outcome = validate_letter(letter, word)

        self.assertEqual(outcome, word)

    def test_in_word(self):
        letter = 'N'
        word = 'BERLIN'
        outcome = validate_letter(letter, word)

        self.assertEqual(outcome, True)

    def test_not_case_sensitive(self):
        letter = 'b'
        word = 'BERLIN'
        outcome = validate_letter(letter, word)

        self.assertEqual(outcome, True)

    def test_not_in_letter(self):
        letter = 'z'
        word = 'BERLIN'
        outcome = validate_letter(letter, word)

        self.assertEqual(outcome, False)


if __name__ == "__main__":
    unittest.main()