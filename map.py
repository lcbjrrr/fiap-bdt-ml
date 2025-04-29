import streamlit as st
import pandas as pd
auto = pd.read_csv("https://raw.githubusercontent.com/lcbjrrr/quantai/refs/heads/main/datasets/autoinsurance.csv")
#st.write(df)
st.map(auto, latitude="lat", longitude="lon", size="2300")
