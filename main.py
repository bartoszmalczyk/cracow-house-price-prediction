import os
import joblib
import pandas as pd
import time

base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, 'model', 'house_prediction_in_cracow.pkl')
engine = joblib.load(model_path)

districts_dict = {
    1: 'district_Bieńczyce', 
    2: 'district_Bieżanów-Prokocim',
    3: 'district_Bronowice', 
    4: 'district_Czyżyny', 
    5: 'district_Dębniki',
    6: 'district_Grzegórzki', 
    7: 'district_Krowodrza', 
    8: 'district_Mistrzejowice',
    9: 'district_Mogilany',
    10: 'district_Niepołomice', 
    11: 'district_Nowa Huta',
    12: 'district_Podgórze', 
    13: 'district_Podgórze Duchackie',
    14: 'district_Prądnik Biały', 
    15: 'district_Prądnik Czerwony',
    16: 'district_Skawina', 
    17: 'district_Stare Miasto', 
    18: 'district_Swoszowice',
    19: 'district_Wieliczka', 
    20: 'district_Wielka Wieś',
    21: 'district_Wzgórza Krzesławickie', 
    22: 'district_Zielonki',
    23: 'district_Zwierzyniec', 
    24: 'district_Łagiewniki-Borek Fałęcki'
}
info = {
    'square footage': [0], 
    'rooms' : [0], 
    'floor' : [0],

    #location
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

    #additional info 
    'has_klima': [0], 
    'has_parking': [0], 
    'has_balkon': [0]
}

clear_command = 'cls' if os.name == 'nt' else 'clear'
def welcome_message():
    print("-" * 50)
    print("         Welcome to house predictor")
    print("answer few questions in order to predict the price")
    print("-" * 50)
    time.sleep(7)
    os.system(clear_command)

if __name__ == "__main__":
    welcome_message()
    for text, parametr in [('What is the ', 'square footage'), ('How many ', 'rooms'), ('On what ', 'floor')]:
        temp = float(input(f"{text}{parametr}: "))
        while temp < 0:
            print("This value cannot be negative! Try again.")
            temp = float(input(f"{text}{parametr}: "))
        info[parametr] = [temp]
        os.system(clear_command)
    os.system(clear_command)
    print("Chose location (just type a number):")
    for number, name in list(districts_dict.items()):
        print(f"{number}.{name}")
    location_nbr = int(input("YOUR ANSWER: "))
    while location_nbr < 1 or location_nbr > 24:
        print("You have inserted the wrong number!")
        location_nbr = int(input("YOUR ANSWER: "))
    info[location_nbr] = [1]
    os.system(clear_command)
# VALIDATION HERE !!!
    print("Tell me if the house has (1 - YES), (0 - NO):")
    info['has_balkon'] = int(input("A balcony? "))
    info['has_parking'] = int(input("A parking slot? "))
    info['has_klima'] = int(input("An airconditioner? "))

    input_df = pd.DataFrame(info)
    prediction_array = engine.predict(input_df)
    estimated_price = prediction_array[0]
    print(f"The price is likely: {round(estimated_price, 2)} PLN")