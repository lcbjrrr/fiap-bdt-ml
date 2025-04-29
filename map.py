import streamlit as st
import pandas as pd
auto = pd.read_csv("autoinsurance.csv")
#st.write(df)
st.map(auto, latitude="lat", longitude="lon", size="2300")
