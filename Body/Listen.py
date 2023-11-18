import speech_recognition as sr
import eel
 
@eel.expose

def Listen():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            eel.DisplayMessage("Recognizing...")
            query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
            print(f"Afzal: {query}\n")  # User query will be printed.
            eel.DisplayMessage(query)
            # eel.ShowHood()

        except Exception as e:
            # print(e)
            print("Say that again please...")  # Say that again will be printed in case of improper voice
            eel.DisplayMessage("Say that again please...")
            return "None"  # None string will be returned
        return query

# while True:
#     Listen()


