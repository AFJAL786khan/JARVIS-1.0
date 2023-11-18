import phonenumbers
  
# geocoder: to know the specific 
# location to that phone number
from phonenumbers import geocoder,carrier


  
   
phone_number = phonenumbers.parse("+1 9123214937") 
# Indian phone number example: +91**********
# Nepali phone number example: +977********** 
   
Carrier = carrier.name_for_number(phone_number, 'en')
print(Carrier)
# this will print the country name
print(geocoder.description_for_number(phone_number, 'en'))   
