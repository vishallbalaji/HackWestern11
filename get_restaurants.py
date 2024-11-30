import requests
import json


def get_restaurants():
  restaurents = []
  url = "https://api.foursquare.com/v3/places/search?ll=42.9849%2C-81.2453&radius=40000&categories=13065"

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