from googletrans import Translator

def hindi_to_english(text):
    translator = Translator()
    translation = translator.translate(text, src='hi', dest='en')
    return translation.text


english_translation = hindi_to_english()

print(f'English: {english_translation}')

