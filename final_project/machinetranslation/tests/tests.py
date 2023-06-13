import unittest

from translator import english_to_french, french_to_english

class TestEtoFTranslator(unittest.TestCase):
    def test_english_to_french_hello(self):
        self.assertEqual(english_to_french('hello'), 'bonjour')

class TestFtoETranslator(unittest.TestCase):
    def test_french_to_english_bonjour(self):
        self.assertEqual(french_to_english('bonjour'), 'hello')

unittest.main()