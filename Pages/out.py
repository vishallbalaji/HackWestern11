import streamlit as st
import pandas as pd
import numpy as np
from get_restaurants import get_restaurants
import ssl
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderServiceError

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

st.title("Search for restaurant")
map_a = pd.DataFrame({
    'latitude': [42.9849, 42.9871, 42.9807],  # Example points in London, Ontario
    'longitude': [-81.2453, -81.2435, -81.2501]
})
st.map(map_a, size=20, color="#0044ff")

# st.button("Reset", type="primary")
if st.button("Get restaurants"):
    get = get_restaurants()
    df = pd.DataFrame(get)
    edited_df = st.data_editor(df) # 👈 An editable dataframe    



st.page_link("streamlit_app.py", label="Home", icon="🏠")





