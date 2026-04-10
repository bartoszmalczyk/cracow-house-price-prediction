import os
import time
import random 
import pandas as pd
from otodom_parser import parse_page


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)
DATA_RAW_DIR = os.path.join(PROJECT_DIR, 'data', 'raw')
os.makedirs(DATA_RAW_DIR, exist_ok=True)

PROGRESS_FILE = os.path.join(BASE_DIR, 'general_last_page.txt') 
DATA_FILE = os.path.join(DATA_RAW_DIR, 'otodom_scraped_data.csv') 

def save_stage(page, PROGRESS_FILE):
    with open(PROGRESS_FILE, "w") as file:
        file.write(str(page))

def load_state(PROGRESS_FILE):
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r') as file:
            return int(file.read().strip())
    return 1
    
start = load_state(PROGRESS_FILE)
total_pages = 269
base_url = "https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/malopolskie/krakow/krakow/krakow?limit=48&page="

for page in range(start + 1, total_pages + 1):
    print(f"{page} / {total_pages}")
    url = base_url + str(page)
    data = parse_page(url)
    
    if data is not None and len(data) > 0:
        df = pd.DataFrame(data)
        df.to_csv(DATA_FILE, mode = 'a', index = False, header = None)
        save_stage(page, PROGRESS_FILE)
    else:
        print(f"Unkown error. Stopped at: {page}")
        break
    time.sleep(random.uniform(4,9))

print("done")
