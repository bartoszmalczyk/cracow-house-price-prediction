import streamlit as st
import pandas as pd

st.set_page_config(
    page_title = "Cracow Real Estate",
    page_icon = "🏠",
    layout = "centered"
)

st.title("Cracow Apartment Valuation")
welcome_text = """
Hello there! This app will help you to estimate the price of the house in Cracow. Firstly, the engine needs some info in order to give its prediction (e.g. square footage, number of rooms, location etc).
"""

st.write(welcome_text)
st.divider()

st.subheader('Size of the apartment')
square_footage = st.number_input("What is the square footage (m²)?", min_value=10.0, max_value=500.0, value=50.0, step=0.5)
st.divider()

st.subheader('Number of rooms')
rooms = st.slider("How many rooms does your apartment have?", 1, 10, 5)
st.divider()

st.subheader('Floor')
floor = st.slider("Which floor is the apartment on? (11 means +10)", 0, 11, 5)
st.divider()

st.subheader('Additional information')
st.write ('Does your apartament has any of the features mentioned underneath?')

balcony = st.checkbox('A balcony')
parking_slot = st.checkbox('A parking slot')
air_conditioner = st.checkbox('An air conditioner')

