# INTERNAL PACKAGES
from Body.Listen import Listen
from Body.Listen import Listen
from Body.Speak import Speak
from Features.WishMe import Wish_Me
from Features.WhatsappAutoMessage import WhatMsg
from Features.EmailAutomation import Email
from Features.Calculator import Calco
from Features.Temperature import Temp
from Features.Location import My_location
from Features.news import news_fetcher
from Features.GoogleMaps import GOOGLE_MAPS
# from Features.Advance_Search import advSearch
# from Brain.Bard_AI import bard_func
# from Brain.GPT import GPT_Brain


# EXTERNAL PACKAGES
import threading
import requests
import datetime
import webbrowser
import pywhatkit
import os
import wikipedia
from time import sleep
import pyautogui
import sys
import psutil
import speedtest
import pyjokes
from PyDictionary import PyDictionary

import eel

@eel.expose



def MAIN():

    print("""
░░░░░██╗░░░░█████╗░░░░██████╗░░░░██╗░░░██╗░░░██╗░░░░██████╗
░░░░░██║░░░██╔══██╗░░░██╔══██╗░░░██║░░░██║░░░██║░░░██╔════╝
░░░░░██║░░░███████║░░░██████╔╝░░░╚██╗░██╔╝░░░██║░░░╚█████╗░
██╗░░██║░░░██╔══██║░░░██╔══██╗░░░░╚████╔╝░░░░██║░░░░╚═══██╗
╚█████╔╝██╗██║░░██║██╗██║░░██║██╗░░╚██╔╝░░██╗██║██╗██████╔╝
░╚════╝░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝╚═╝╚═╝╚═════╝░""")

    Wish_Me()
    while True:
        query = Listen().lower()

# TELLS TIME
        if 'time' in query:
            Time = datetime.datetime.now().strftime("%H:%M:%S")
            Speak(f"Sir, the time is {Time}")
            print(f"Jarvis: {Time}")

# TEllS CURRENT DATE
        elif 'date' in query:
            day = int(datetime.datetime.now().day)
            month = int(datetime.datetime.now().month)
            year = int(datetime.datetime.now().year)
            Speak('The current date is')
            print(f"jarvis: {day, month, year}")
            Speak(f"{day}|{month}|{year}")

# CONTROL VOLUME
        elif 'volume up' in query:
            pyautogui.press("vloumeup")
        elif 'volume down' in query:
            pyautogui.press("volumedown")
        elif 'volume mute' in query:
            pyautogui.press("vloumemute")

# TELLS BATTERY PERCENTAGE
        elif 'how much power left' in query or 'how much power we have' in query or 'battery percentage' in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            Speak(f"Jarvis: Sir our system have {percentage} percent battery")

# CHECK INTERNET SPEED
        elif 'internet speed' in query:
           
            def internetSpeed():
                st = speedtest.Speedtest()
                dl = st.download()
                up = st.upload()
                Speak(f"Jarvis: Sir we have {dl} bit per secong downloading speed and {up} bit per second uploading speed.")
            internet_speed = threading.Thread(target=internetSpeed)
            internet_speed.start()

# TELLS THE CURRENT LOCATION
        elif 'my location' in query:
            My_location()

# TELLS THE USER IP ADDRESS
        elif 'ip address' in query:
            ip = requests.get('https://api.ipify.org').text
            print(ip)
            Speak(f"Jarvis: Your ip address is  {ip}")

# TELLS THE LATEST NEWS
        elif 'news' in query:
            Speak("Please wait Sir, fetching the latest news")
            news_fetcher()

# GoogleMaps (fetch Distance)
        elif 'distance' in query or 'far' in query:
            query = query.replace('distance', '')
            query = query.replace('Distance', '')
            query = query.replace('far', '')
            query = query.replace('of', '')
            GOOGLE_MAPS(query)

# TELLS A JOKE
        elif 'tell me a joke' in query:
            Speak('Okay Sir')
            joke = pyjokes.get_joke()
            Speak(joke)

# DO CALCULATIONS
        elif "calculate" in query:
            calculation = threading.Thread(target=Calco,args=query)
            calculation.start()

# TELLS TEMPERATURE
        elif 'temperature' in query:
            Temp(query)

# OPENS ANY SOFTWARE, APP OR PROGRAMM
        elif 'open' in query:
            query = query.replace("open", "")
            query = query.replace("jarvis", "")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            # pyautogui.sleep(2)
            pyautogui.press("enter")

# CLOSES ANY SOFTWARE, APP OR PROGRAMM
        elif 'close' in query:
            query = query.replace("close", "")
            query = query.replace("jarvis", "")
            process_name = query
            os.system(f"taskkill /f /im {process_name}.exe")
            Speak(f"Jarvis: Closed {process_name} successfully.")

# SEARCH ANYTHING ON WIKIPEDIA
        elif 'wikipedia' in query:
            def wiki(query_wiki):
                try:
                    Speak('Searching...')
                    query_wiki = query_wiki.replace("wikipedia", "")
                    query_wiki = query_wiki.replace("jarvis", "")
                    query_wiki = query_wiki.replace("search", "")
                    query_wiki = query_wiki.replace("on", "")
                    result = wikipedia.summary(query, sentences=10)
                    Speak(result)
                    
                except Exception as e:
                    Speak('Please Try again. There has been an error')
                    
             
            wiki_thread = threading.Thread(target=wiki, args=(query,))
            wiki_thread.start()
            # while wiki_thread.is_alive() and not stop_flag.clear():
            #     sleep(0.1)
            #     stop_flag.clear()
              
            
# SEARCH ANYTHING ON CHROME
        elif 'search' in query:
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            Speak('What should I search ?')
            search = Listen().lower()
            webbrowser.get(chrome_path).open_new_tab(search + ".com")

# SEARCH ANYTHING ON GOOGLE
        elif 'google' in query:
            query = query.replace('Google', '')
            query = query.replace('google', '')
            query = query.replace('search', '')
            query = query.replace('on', '')
            question = query
            Speak(f'Searching {query} on google')
            search_url = f"https://www.google.com/search?q={question}"
            webbrowser.open_new_tab(search_url)

# PLAYS ANY SONG ON YOUTUBE
        elif 'song' in query or 'music' in query or 'YouTube' in query:
            query = query.replace('Song', '')
            query = query.replace('Music', '')
            query = query.replace('Play', '')
            query = query.replace('on', '')
            # Speak('Sir which Song you would like to listen.')
            SongName = query
            pywhatkit.playonyt(SongName)

# SEND AUTOMATED MESSAGES ON WHATSAPP
        elif 'send whatsapp' in query:
            whatsapp_threading = threading.Thread(target=WhatMsg)
            whatsapp_threading.start()
            # WhatMsg()

# SEND AUTOMATED EMAILS
        elif 'send email' in query:
            Email()

# Dictionary
        elif 'meaning of' in query:
            try:
                dict = PyDictionary()
                query = query.replace('what', '')
                query = query.replace('is', '')
                query = query.replace('the', '')
                query = query.replace('meaning', '')
                query = query.replace('this', '')
                query = query.replace('word', '')
                query = query.replace('of', '')
                dict_answer = query
                meaning = dict.meaning(str(dict_answer))
                Speak(meaning)
            except Exception:
                print('There Has been some Error')
                Speak('There Has been some Error')

# PYAUTOGUI FEATURES ---
        elif 'hidden menu' in query:
            # Win + x : open the hidden menu
            pyautogui.hotkey('winleft', 'x')

        elif 'task manager' in query:
            # CTRL + shift + ESC : open task manager
            pyautogui.hotkey('ctrl', 'shift', 'esc')

        elif 'task view' in query:
            # Win + tab : open the task view
            pyautogui.hotkey('winleft', 'tab')

        elif 'screenshot' in query:
            img = pyautogui.screenshot()
            img.save('D:/MyData/Documents/CODING/Python/Jarvis/Data/Screenshots/ss.png')
            Speak('Done')

        elif 'close the app' in query:
            pyautogui.hotkey('alt', 'f4')

        elif 'new virtual desktop' in query:
            pyautogui.hotkey('winleft', 'ctrl', 'd')


# SHUTDOWN FEATURES ---

        elif 'logout' in query:
            Speak('logging out in 5 seconds')
            sleep(5)
            os.sys('shutdown - l')

        elif 'shutdown' in query:
            Speak('Shutting down in 5 seconds')
            sleep(5)
            os.system('shutdown /s /t 1')

        elif 'restart' in query:
            Speak('restarting in 5 seconds')
            sleep(5)
            os.sys('shutdown /r /t 1')

        elif 'sleep' in query:
            Speak("Okay Sir I am going to Sleep; you can call me anytime.")
            break

# Advance Search
        else:
            pass
            # GPT_Brain(query)
            # bard_func(query)
        

# MAIN()

# if __name__ == "__main__":
@eel.expose

def Jarvis():
    while True:
        query = Listen().lower()
        if "wake up" in query:
            MAIN()
        elif "goodbye" in query:
            print('Good Bye Sir; Have a Nice Day.')
            Speak('Good Bye Sir; Have a Nice Day.')
            sys.exit()


# Jarvis()

