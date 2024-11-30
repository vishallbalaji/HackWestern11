import streamlit as st
from get_restaurants import get_restaurants
import pandas as pd

get = get_restaurants()


df = pd.DataFrame(get)
edited_df = st.data_editor(df) # 👈 An editable dataframe

favorite_command = edited_df.loc[edited_df["name"].idxmax()]["address"]

