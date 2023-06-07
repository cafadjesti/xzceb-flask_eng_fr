"""
This module contains two functions for translating English text to French and vice versa.
It uses MyMemoryTranslator from the deep_translator package.
"""

from deep_translator import MyMemoryTranslator



def english_to_french(english_text):
    """
    Translate English text to French using MyMemoryTranslator.
    """
    print(f"Translating '{english_text}' from English to French.")
    translator = MyMemoryTranslator(source='english', target='french')
    french_text = translator.translate(english_text)
    print(f"The translated text is '{french_text}'.")
    return french_text


def french_to_english(french_text):
    """
    Translate French text to English using MyMemoryTranslator.
    """
    
    translator = MyMemoryTranslator(source='french', target='english')
    english_text = translator.translate(french_text)
    return english_text
