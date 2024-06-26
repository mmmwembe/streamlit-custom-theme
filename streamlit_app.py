import streamlit as st
import pymongo
from pymongo import MongoClient


st.title('Customizing the theme of Streamlit apps')

st.write('Contents of the `.streamlit/config.toml` file of this app')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('Confidence Threshold:', 0.1, 1.0, 0.5)
st.write('Selected number from slider widget is:', number)
