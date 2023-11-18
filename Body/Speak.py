import pyttsx3
import eel

@eel.expose

def Speak(text):

# Initializing the Voice Engine
    engine = pyttsx3.init('sapi5')

# Rate
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 175)

# Volume
    volume = engine.getProperty('volume')
    engine.setProperty('volume', 1.0)


# Changing Voice
    voices = engine.getProperty('voices', )
    engine.setProperty('voice', voices[0].id)
    print(f"Jarvis: {text}")
    eel.DisplayMessage(text)
    engine.say(text)

    engine.runAndWait()



# Speak('जार्विस आज टाइम क्या है')

# Speak("I am Jarvis How can I help you")
