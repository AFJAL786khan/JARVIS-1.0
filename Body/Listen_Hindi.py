import speech_recognition as sr
from googletrans import Translator
# import eel

import eel

@eel.expose

def Listen_Hindi():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            eel.DisplayMessage("Recoginizing...")
            query = r.recognize_google(audio, language='hi')  # Using google for voice recognition.


            # Create a Translator object
            translator = Translator()

            # Input Hindi text
            hindi_text = query

            # Translate to English
            translation = translator.translate(hindi_text, src='hi', dest='en')

            # Get the translated text
            english_translation = translation.text

            print(f"Afzal: {english_translation}\n")  # User query will be printed.
            eel.DisplayMessage(english_translation)
            eel.ShowHood()

        except Exception as e:
            # print(e)
            print("Say that again please...")  # Say that again will be printed in case of improper voice
            return "None"  # None string will be returned
        return english_translation



# while True:
#     Listen_Hindi()



