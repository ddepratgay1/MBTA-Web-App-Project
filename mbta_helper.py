import os
from dotenv import load_dotenv
import urllib.request
import json
import urllib.parse

# Load environment variables
load_dotenv()

# Get API keys from environment variables
MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")
MBTA_API_KEY = os.getenv("MBTA_API_KEY")

# Useful base URLs (you need to add the appropriate parameters for each API request)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


# A little bit of scaffolding if you want to use it
def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_lng() and get_nearest_station() might need to use this function.
    """
    with urllib.request.urlopen(url) as response:
        response_text = response.read().decode("utf-8")
        return json.loads(response_text)


def get_lat_lng(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    place_encoded = urllib.parse.quote(place_name)
    url = f"{MAPBOX_BASE_URL}/{place_encoded}.json?access_token={MAPBOX_TOKEN}"

    print("Requesting URL:", url)
    data = get_json(url)
    print("Response JSON:", data)

    if not data["features"]:
        raise ValueError(f"No location data found for '{place_name}'")
    
    coordinates = data["features"][0]["geometry"]["coordinates"]
    return str(coordinates[1]), str(coordinates[0])


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    url = f"{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance"

    data = get_json(url)
    stop_name = data["data"][0]["attributes"]["name"]
    wheelchair = data["data"][0]["attributes"]["wheelchair_boarding"]
    accessible = wheelchair == 1 # 1 = accessible, 2 = not accessible, 0 = no info

    return stop_name, accessible


def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    lat, lon = get_lat_lng(place_name)
    return get_nearest_station(lat, lon)


def main():
    """
    You should test all the above functions here
    """
    place = "Fenway Park, Boston"
    stop, accessible = find_stop_near(place)
    print(f"Nearest stop to {place}: is '{stop}'")
    print(f"Wheelchair accessible?" , "Yes" if accessible else "No")


if __name__ == "__main__":
    main()
