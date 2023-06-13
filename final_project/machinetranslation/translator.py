"""Module for translating text between English and French."""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translates English text to French.

    Args:
        englishText (str): The English text to translate.

    Returns:
        str: The French translation of the input text.
    """
    #Per deep-translator project page:
    #https://deep-translator.readthedocs.io/en/latest/README.html#id2
    french_text = MyMemoryTranslator(source='en', target='fr').translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    Translates French text to English.

    Args:
        frenchText (str): The French text to translate.

    Returns:
        str: The English translation of the input text.
    """
    #Per deep-translator project page:
    #https://deep-translator.readthedocs.io/en/latest/README.html#id2
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text
