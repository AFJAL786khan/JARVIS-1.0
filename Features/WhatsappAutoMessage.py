import pywhatkit
from Body.Listen_Hindi import Listen_Hindi
from Body.Speak import Speak
from datetime import timedelta
from datetime import datetime

# Create a dictionary to store the numbers of different people
contacts = {
    'John': '+1234567890',  # Replace with actual numbers
    'Alice': '+91 6367454630',  # Replace with actual numbers
    # Add more contacts as needed
}

def WhatMsg():
    try:
        Speak('Whom do you want to send a message to?')
        person = Listen_Hindi()

        # Check if the person exists in the contacts
        if person in contacts:
            Speak('What message should I send?')
            message = Listen_Hindi()
            number = contacts[person]  # Get the person's number from the dictionary

            minute = int((datetime.now() + timedelta(minutes=1.5)).strftime("%M"))
            hour = int(datetime.now().strftime("%H"))

            pywhatkit.sendwhatmsg(number, message, time_hour=hour, time_min=minute, wait_time=1)

            Speak('Message sent.')

        else:
            Speak('Sorry, I dont have this person in my contacts.')

    except Exception as e:
        Speak('There has been an error.')
        print('There has been an error:', str(e))

# WhatMsg()
