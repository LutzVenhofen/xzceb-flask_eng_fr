import unittest
from translator import english_to_french, french_to_english


class TestEnglishToFrench(unittest.TestCase):
    def test_translate_hello(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
    
    def test_null(self):
        self.assertEqual(english_to_french(None), None)

class TestFrenchToEnglish(unittest.TestCase):
    def test_translate_bonjour(self):
        self.assertEqual(french_to_english("Bonjour"), "Bonjour")
    
    def test_null(self):
        self.assertEqual(french_to_english(None), None)