import os
import time
import random
import pandas as pd
from general_scraper import save_stage 
from general_scraper import load_state
from otodom_parser import parse_offer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_CSV = os.path.join(BASE_DIR, "..", "data", "raw", "otodom_scraped_data.csv")
PROGRESS_FILE = os.path.join(BASE_DIR, 'detail_last_page.txt')
OUTPUT_CSV = os.path.join(BASE_DIR, "..", "data", "raw", "only_details.csv")

df = pd.read_csv(INPUT_CSV)
slugs = df["slug"]
start = load_state(PROGRESS_FILE)

for index in range(start, len(slugs)):
    slug = slugs.iloc[index]
    print(f"{index} / {len(slugs)}")
    new_details = parse_offer(slug)
    if new_details:
        new_details["slug"] = slug 
        df_out = pd.DataFrame([new_details])
        df_out.to_csv(OUTPUT_CSV, mode='a', index=False, header=not os.path.exists(OUTPUT_CSV))
        df.to_csv(OUTPUT_CSV, mode = 'a', index = False, header = None)
        save_stage(index + 1, PROGRESS_FILE)
    else:
        print("Error, slug : {slug}")
    time.sleep(random.uniform(3,5))


"""
//TODO: 
1. connect new data with old csv and put it into new csv file: full_data.csv
2. create a new model which can deduce if the output shows the interior or not
3. scrap all photos into 3 categories: premium / standard / raw state
"""


