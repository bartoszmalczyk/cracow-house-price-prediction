import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

def get_json_data(url):
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
    return raw_json 

 # general info parsing  
def parse_page(url):    
    raw_json = get_json_data(url)
    try:
        listings = raw_json['props']['pageProps']['data']['searchAds']['items']
    except KeyError:
        print(KeyError)
        return None
    
    data_list = []
    for item in listings:
        flat_data = {
            'slug': item.get('slug'),
            'tytul': item.get('title'),
            'cena': item.get('totalPrice', {}).get('value') if item.get('totalPrice') else None,
            'metraz': item.get('areaInSquareMeters'),
            'pokoje': item.get('roomsNumber'),
            'pietro': item.get('floorNumber'),
            'dzielnica': item.get('location', {}).get('reverseGeocoding', {}).get('locations', [{}])[-2].get('name', 'Brak'),
        }
        data_list.append(flat_data)
    return pd.DataFrame(data_list)

# single offer parsing
def parse_offer(slug):
    url = f"https://www.otodom.pl/pl/oferta/{slug}"
    try:
        raw_json = get_json_data(url)
        if not raw_json:
            return None
        
        data = raw_json['props']['pageProps']['ad']
        details_info = data.get('target', {})
        
        def get_first(key):
            val = details_info.get(key)
            return val[0] if isinstance(val, list) and len(val) > 0 else val

        build_year = get_first('Build_year')
        market = get_first('MarketType')
        extras_list = details_info.get('Extras_types', [])
        pietro = get_first('Floor_no')
        building_type = get_first('Building_type')
        heating = get_first('Heating')
        construction_status = get_first('Construction_status')

        photos = data.get('images', [])

        ans = []
        for i in photos:
            large = i.get('large')
            if large and "projection" not in large.lower() and "plan" not in large.lower():
                ans.append(large)
                
        details = {
            'market': market,
            'build_year': build_year,
            'type': building_type,
            'heating': heating,
            'stan_wykonczenia': construction_status,
            'extras': ",".join(extras_list) if isinstance(extras_list, list) else extras_list,
            'photos': ",".join(ans)
        }
        return details
        
    except Exception as e:
        # Dodane 'f' z przodu, żeby zmienne w klamrach zadziałały
        print(f"Error occurred at {slug}: {e}") 
        return None
    
if __name__ == "main":
    url = "https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/malopolskie/krakow"
    df = parse_page(url)

    if df is not None:
        print(df.head())
        df.to_csv("first_page_cracow.csv", index = False)