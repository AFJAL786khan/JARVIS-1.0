import requests
from Body.Speak import Speak
import webbrowser

def My_location():
    try:
        ip_add = requests.get("https://api.ipify.org").text
        url = "https://get.geojs.io/v1/ip/geo/"  + ip_add + '.json'
        geo_q = requests.get(url)
        geo_d = geo_q.json()
        # city = geo_d['city']
        country = geo_d['country']
        latitude = geo_d['latitude']
        longitude = geo_d['longitude']
        op = f"https://www.google.com/maps/place/MIDWAY+HOTEL/@{latitude},{longitude},17z/data=!3m1!4b1!4m5!3m4!1s0x3973ff108ac4be7f:0x1bb99a26b4dc1f5d!8m2!3d26.714561!4d77.8951871"
        webbrowser.open(op)
        Speak(f"Sir, You are now in Dholpur {country}")

    except Exception:
        Speak("There has been some error")


