import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
data = []
def parse_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return None 
    
    soup = BeautifulSoup(response.text, 'html.parser')
    script_tag = soup.find('script', id = '__NEXT_DATA__')

    if not script_tag:
        print("Error - there is no __NEXT_DATA__ tag")
        return None

    raw_json = json.loads(script_tag.string)
    
    try:
        listings = raw_json['props']['pageProps']['data']['searchAds']['items']
    except KeyError:
        print(KeyError)
        return None
    
    data_list = []
    for item in listings:
        flat_data = {
            'id': item.get('id'),
            'tytul': item.get('title'),
            'cena': item.get('totalPrice', {}).get('value') if item.get('totalPrice') else None,
            'waluta': item.get('totalPrice', {}).get('currency') if item.get('totalPrice') else None,
            'metraz': item.get('areaInSquareMeters'),
            'pokoje': item.get('roomsNumber'),
            'pietro': item.get('floorNumber'),
            'dzielnica': item.get('location', {}).get('reverseGeocoding', {}).get('locations', [{}])[-2].get('name', 'Brak'),
        }
        data_list.append(flat_data)
    
    return pd.DataFrame(data_list)

if __name__ == "main":
    url = "https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/malopolskie/krakow"
    df = parse_page(url)

    if df is not None:
        print(df.head())
        df.to_csv("first_page_cracow.csv", index = False)