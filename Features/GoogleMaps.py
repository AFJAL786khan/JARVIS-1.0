import requests
import webbrowser
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut  # Import GeocoderTimedOut exception
from geopy.distance import great_circle
from Body.Speak import Speak

# Function to get your current location
def GOOGLE_MAPS(location_name):

    def get_current_location():
        ip_address = requests.get("https://api.ipify.org").text
        url = "https://get.geojs.io/v1/ip/geo/" + ip_address + '.json'
        geo_q = requests.get(url)
        geo_d = geo_q.json()
        return geo_d

    # Function to geocode a location name to coordinates
    def geocode_location_name(location_name):
        geolocator = Nominatim(user_agent="location_app")

        try:
            location = geolocator.geocode(location_name)
            if location:
                return location.latitude, location.longitude
            else:
                print("Location not found.")
                return None, None
        except GeocoderTimedOut:
            print("Geocoding service timed out.")
            return None, None

    # Function to calculate the distance between two locations
    def calculate_distance(current_location, destination_location):
        current_coords = (current_location['latitude'], current_location['longitude'])
        destination_coords = geocode_location_name(destination_location)

        if None not in destination_coords:
            distance = great_circle(current_coords, destination_coords).kilometers
            return int(distance)
        else:
            return None

    # Get your current location
    current_location = get_current_location()

    # Specify the destination location by name
    destination_location_name = location_name

    # Calculate the distance
    distance = calculate_distance(current_location, destination_location_name)
    distance = distance

    if distance is not None:
        # Open the destination location in Google Maps
        op = f"https://www.google.com/maps/place/{destination_location_name.replace(' ', '+')}"
        webbrowser.open(op)

        # Speak the results
        print(f"Your current location: Latitude {current_location['latitude']}, Longitude {current_location['longitude']}")
        # Speak(f"Your current location: Latitude {current_location['latitude']}, Longitude {current_location['longitude']}")

        print(f"{destination_location_name} is {distance} Kilometers away from your location")
        Speak(f"{destination_location_name} is {distance} Kilometers away from your location")

# GOOGLE_MAPS('paris')