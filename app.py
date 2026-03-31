import streamlit as st
import pandas as pd
import folium
import os
import joblib
from streamlit_folium import st_folium
from district_cords import district_coords

@st.cache_resource
def load_model():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(base_dir, 'model', 'house_prediction_in_cracow.pkl')
    return joblib.load(model_path)
engine = load_model()

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

st.divider()
st.subheader('Location')
st.write ('Please select in which district your apartment is located in:')

if 'selected_district' not in st.session_state:
    st.session_state.selected_district = None

cracow_map = folium.Map(location=[50.0614, 19.9372], zoom_start=12)

for district_name, coords in district_coords.items():
    clean_name = district_name.replace('district_', '')
    
    folium.Marker(
        location=coords,
        tooltip=clean_name, # This text pops up when hovering/clicking
        icon=folium.Icon(color="oranges", icon="info-sign")
    ).add_to(cracow_map)

map_data = st_folium(cracow_map, width=700, height=400)

if map_data['last_object_clicked_tooltip']:
    clicked_name = map_data['last_object_clicked_tooltip']
    st.session_state.selected_district = f"district_{clicked_name}"

if st.session_state.selected_district:
    display_name = st.session_state.selected_district.replace('district_', '')
    st.success(f"📍 Selected location: {display_name}")
else:
    st.warning("Please click on a red pin on the map to select a district.")

st.divider()
st.write("We are all set! Now you can check the price!")
if st.button("Estimate the price!", type="primary", use_container_width=True):    
    if st.session_state.selected_district is None:
        st.error("You must have forgotten to choose the district")
    else:
        payload = {
            'square footage': [square_footage], 
            'rooms' : [rooms], 
            'floor' : [floor],
            'district_Bieńczyce' : [0], 
            'district_Bieżanów-Prokocim' : [0],
            'district_Bronowice': [0], 
            'district_Czyżyny': [0], 
            'district_Dębniki': [0],
            'district_Grzegórzki': [0], 
            'district_Krowodrza': [0], 
            'district_Mistrzejowice': [0],
            'district_Mogilany' : [0],
            'district_Niepołomice': [0], 
            'district_Nowa Huta': [0],
            'district_Podgórze': [0], 
            'district_Podgórze Duchackie': [0],
            'district_Prądnik Biały': [0], 
            'district_Prądnik Czerwony': [0],
            'district_Skawina': [0], 
            'district_Stare Miasto': [0], 
            'district_Swoszowice': [0],
            'district_Wieliczka': [0], 
            'district_Wielka Wieś': [0],
            'district_Wzgórza Krzesławickie': [0], 
            'district_Zielonki': [0],
            'district_Zwierzyniec': [0], 
            'district_Łagiewniki-Borek Fałęcki': [0],

            'has_klima': [int(air_conditioner)], 
            'has_parking': [int(parking_slot)], 
            'has_balkon': [int(balcony)]
        }
        payload[st.session_state.selected_district] = [1]
        

        input_df = pd.DataFrame(payload)
        prediction = engine.predict(input_df)[0]
        
        st.success(f"Estimated price: {prediction:,.0f} PLN".replace(',', ' '))
        st.balloons()