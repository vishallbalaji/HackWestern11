import streamlit as st
import pandas as pd
import numpy as np
from get_restaurants import get_restaurants,get_coordinates,check_and_remove_parentheses


st.title("Search for restaurant")

if st.button("Get restaurants"):
    get = get_restaurants()
    lat = []
    lon = []
    df = pd.DataFrame(get)
    edited_df = st.data_editor(df) # 👈 An editable dataframe    
    for e in get:
        address = e['address'][:-8]
        newadd = check_and_remove_parentheses(address)
        cor = get_coordinates(newadd)
        lat.append(cor[0])
        lon.append(cor[1])

    map_a = pd.DataFrame({
        'latitude': lat,  # Example points in London, Ontario
        'longitude': lon
    })
    st.map(map_a, size=20, color="#0044ff")

st.page_link("streamlit_app.py", label="Home", icon="🏠")
