import requests
import json
import ssl
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderServiceError
import re

def get_coordinates(address):
    geolocator = Nominatim(user_agent="geoapi", timeout=10)
    try:
        ssl._create_default_https_context = ssl._create_unverified_context
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        else:
            return None
    except GeocoderServiceError as e:
        print(f"Geocoding error: {e}")
        return None
    
def check_and_remove_parentheses(text):
    """Check if the text contains parentheses, and if so, remove them and their content."""
    if "(" in text and ")" in text:  
        return re.sub(r"\([^)]*\)", "", text)  
    else:
        return text  
    
def get_restaurants(la,lo):
  restaurents = []
  url = f"https://api.foursquare.com/v3/places/search?ll={la}%2C{lo}&radius=40000&categories=13065"

  headers = {
    'Content-Type': 'application/json',
    'Authorization': 'fsq3UxPR9u3RpAZm/enwztinyyEQJXR7P9Zl/4g9UOSlcLc='
  }

  response = requests.request("GET", url, headers=headers)

  rests = json.loads(response.text)

  allrest = rests['results']
  for r in allrest:
      rInfo = { 'name': r['name'],
                'open': r['closed_bucket'],
                'address': r['location']['formatted_address']}
      restaurents.append(rInfo)
      # print(r['name'])
      # print(r['closed_bucket'])
      # print(r['location']['formatted_address'])
        # eachCat = r['categories']
        # for c in eachCat:
          #  print(c['name'])
          #  print(c[''])
  # print(restaurents)
  return restaurents

# get = get_restaurants()
# print(get)