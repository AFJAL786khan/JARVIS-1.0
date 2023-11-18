import datetime
from Body.Speak import Speak
from playsound import playsound

def Wish_Me():
    audio_file = r'D:\MyData\Documents\CODING\Python\Jarvis\Data\Music\Jarvis-StartUp-Sound.mp3'
    playsound(audio_file)

    hour = int(datetime.datetime.now().hour)

    if hour >= 6 and hour <= 12:
        Speak('Good Morning Sir!')

    elif hour >= 12 and hour <= 18:
        Speak('Good Afternoon Sir!')

    elif hour >= 18 and hour <= 24:
        Speak('Good Evening Sir!')

    else:
        Speak('Good Night')

    Speak('I am Jarvis, your trusted virtual assistant. How Can I help you Today ?')


