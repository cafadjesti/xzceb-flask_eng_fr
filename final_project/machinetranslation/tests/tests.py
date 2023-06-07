"""
This module contains unittests for the translation functions in the translator.py module.
"""

import unittest
from translator import french_to_english, english_to_french


class TestTranslatorFunctions(unittest.TestCase):
    """
    This class contains unittests for the translation functions in translator.py.
    """

    def test_english_to_french(self):
        """
        Test the english_to_french function.
        """
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('Programming is cool'), 'La programmation c\'est cool')

    def test_french_to_english(self):
        """
        Test the french_to_english function.
        """
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('La programmation c\'est cool'), 'Programming is cool')
    
unittest.main()
