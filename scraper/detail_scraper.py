import os
import time
import random
import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
from otodom_parser import get_json_data

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_CSV = os.path.join(BASE_DIR, "ot")
                           
def details_download(slug):
    url = f"https://www.otodom.pl/pl/oferta/{slug}"
    raw_json = get_json_data(url)
    data = raw_json['props']['pageProps']['ad']
    details_info = data.get('target',{})
    details = {
        'build_year' : details_info.get('Build_year'),
        'extras' : details_info.get('Extras_types'),
        'market' : details_info.get('MarketType'),
    }
    photos = raw_json['props']['pageProps']['ad']['images']
    links = photos.get("large")
    print(links)

details_download("2-pokojowe-mieszkanie-45m2-balkon-bezposrednio-ID4yTxi")


"""
[{'thumbnail': 'https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6ImQyOXRwZ3A4enNqdy1FQ09TWVNURU0iLCJ3IjpbeyJmbiI6ImVudmZxcWUxYXk0azEtQVBMIiwicyI6IjE0IiwicCI6IjEwLC0xMCIsImEiOiIwIn1dfQ.2T1RThQIseIwAUct7dabnCp_kilJJeCa1WYKwrgXXN4/image;s=184x138;q=80', 
'small': 'https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6ImQyOXRwZ3A4enNqdy1FQ09TWVNURU0iLCJ3IjpbeyJmbiI6ImVudmZxcWUxYXk0azEtQVBMIiwicyI6IjE0IiwicCI6IjEwLC0xMCIsImEiOiIwIn1dfQ.2T1RThQIseIwAUct7dabnCp_kilJJeCa1WYKwrgXXN4/image;s=314x236;q=80', 
'medium': 'https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6ImQyOXRwZ3A4enNqdy1FQ09TWVNURU0iLCJ3IjpbeyJmbiI6ImVudmZxcWUxYXk0azEtQVBMIiwicyI6IjE0IiwicCI6IjEwLC0xMCIsImEiOiIwIn1dfQ.2T1RThQIseIwAUct7dabnCp_kilJJeCa1WYKwrgXXN4/image;s=655x491;q=80', 
'large': 'https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6ImQyOXRwZ3A4enNqdy1FQ09TWVNURU0iLCJ3IjpbeyJmbiI6ImVudmZxcWUxYXk0azEtQVBMIiwicyI6IjE0IiwicCI6IjEwLC0xMCIsImEiOiIwIn1dfQ.2T1RThQIseIwAUct7dabnCp_kilJJeCa1WYKwrgXXN4/image;s=1280x1024;q=80', '__typename': 'AdImage'},
{'thumbnail': 'https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6Iml4cmQwYnl6dXY0dTItRUNPU1lTVEVNIiwidyI6W3siZm4iOiJlbnZmcXFlMWF5NGsxLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.TsDE2E60yRQZ0YacDU3ayTfTbYl7XNIdg9PXAPc-rwk/image;s=184x138;q=80',
'small': 'https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6Iml4cmQwYnl6dXY0dTItRUNPU1lTVEVNIiwidyI6W3siZm4iOiJlbnZmcXFlMWF5NGsxLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.TsDE2E60yRQZ0YacDU3ayTfTbYl7XNIdg9PXAPc-rwk/image;s=314x236;q=80',
'medium': 'https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6Iml4cmQwYnl6dXY0dTItRUNPU1lTVEVNIiwidyI6W3siZm4iOiJlbnZmcXFlMWF5NGsxLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.TsDE2E60yRQZ0YacDU3ayTfTbYl7XNIdg9PXAPc-rwk/image;s=655x491;q=80', 
'large': 'https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6Iml4cmQwYnl6dXY0dTItRUNPU1lTVEVNIiwidyI6W3siZm4iOiJlbnZmcXFlMWF5NGsxLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.TsDE2E60yRQZ0YacDU3ayTfTbYl7XNIdg9PXAPc-rwk/image;s=1280x1024;q=80', '__typename': 'AdImage'}, 
{'thumbnail': 'https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6IjFxYXQwZDY1MXV2bzItRUNPU1lTVEVNIiwidyI6W3siZm4iOiJlbnZmcXFlMWF5NGsxLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.3VC022De3EyBsEzUeoBr5Y_p4uzU8TZDg2JPOA9SnFo/image;s=184x138;q=80', 
'small': 'https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6IjFxYXQwZDY1MXV2bzItRUNPU1lTVEVNIiwidyI6W3siZm4iOiJlbnZmcXFlMWF5NGsxLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.3VC022De3EyBsEzUeoBr5Y_p4uzU8TZDg2JPOA9SnFo/image;s=314x236;q=80', 
'medium': 'https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6IjFxYXQwZDY1MXV2bzItRUNPU1lTVEVNIiwidyI6W3siZm4iOiJlbnZmcXFlMWF5NGsxLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.3VC022De3EyBsEzUeoBr5Y_p4uzU8TZDg2JPOA9SnFo/image;s=655x491;q=80', 
'large': 'https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6IjFxYXQwZDY1MXV2bzItRUNPU1lTVEVNIiwidyI6W3siZm4iOiJlbnZmcXFlMWF5NGsxLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.3VC022De3EyBsEzUeoBr5Y_p4uzU8TZDg2JPOA9SnFo/image;s=1280x1024;q=80', '__typename': 'AdImage'}, 
{'thumbnail': 'https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6IjYxMWU5aTZkZjJ5dy1FQ09TWVNURU0iLCJ3IjpbeyJmbiI6ImVudmZxcWUxYXk0azEtQVBMIiwicyI6IjE0IiwicCI6IjEwLC0xMCIsImEiOiIwIn1dfQ.Legb90ojftI3WuC5DhUY1b2xFdEBTmFzu6UEn1ZcK6o/image;s=184x138;q=80', 
'small': 'https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6IjYxMWU5aTZkZjJ5dy1FQ09TWVNURU0iLCJ3IjpbeyJmbiI6ImVudmZxcWUxYXk0azEtQVBMIiwicyI6IjE0IiwicCI6IjEwLC0xMCIsImEiOiIwIn1dfQ.Legb90ojftI3WuC5DhUY1b2xFdEBTmFzu6UEn1ZcK6o/image;s=314x236;q=80', 
'medium': 'https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6IjYxMWU5aTZkZjJ5dy1FQ09TWVNURU0iLCJ3IjpbeyJmbiI6ImVudmZxcWUxYXk0azEtQVBMIiwicyI6IjE0IiwicCI6IjEwLC0xMCIsImEiOiIwIn1dfQ.Legb90ojftI3WuC5DhUY1b2xFdEBTmFzu6UEn1ZcK6o/image;s=655x491;q=80', 
'large': 'https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6IjYxMWU5aTZkZjJ5dy1FQ09TWVNURU0iLCJ3IjpbeyJmbiI6ImVudmZxcWUxYXk0azEtQVBMIiwicyI6IjE0IiwicCI6IjEwLC0xMCIsImEiOiIwIn1dfQ.Legb90ojftI3WuC5DhUY1b2xFdEBTmFzu6UEn1ZcK6o/image;s=1280x1024;q=80', '__typename': 'AdImage'},
 {'thumbnail': 'https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6IjZhbW4zb2Q1Mmt4cTEtRUNPU1lTVEVNIiwidyI6W3siZm4iOiJlbnZmcXFlMWF5NGsxLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.9yQKRnidHqIbB6yQIwnCHyzSIw3SIHeqz5Tp6tUKVnc/image;s=184x138;q=80', 
 'small': 'https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6IjZhbW4zb2Q1Mmt4cTEtRUNPU1lTVEVNIiwidyI6W3siZm4iOiJlbnZmcXFlMWF5NGsxLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.9yQKRnidHqIbB6yQIwnCHyzSIw3SIHeqz5Tp6tUKVnc/image;s=314x236;q=80', 
 'medium': 'https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6IjZhbW4zb2Q1Mmt4cTEtRUNPU1lTVEVNIiwidyI6W3siZm4iOiJlbnZmcXFlMWF5NGsxLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.9yQKRnidHqIbB6yQIwnCHyzSIw3SIHeqz5Tp6tUKVnc/image;s=655x491;q=80', 
 'large': 'https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6IjZhbW4zb2Q1Mmt4cTEtRUNPU1lTVEVNIiwidyI6W3siZm4iOiJlbnZmcXFlMWF5NGsxLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.9yQKRnidHqIbB6yQIwnCHyzSIw3SIHeqz5Tp6tUKVnc/image;s=1280x1024;q=80', '__typename': 'AdImage'}, 
 {'thumbnail': 'https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6InBvZ3pqOTRzcm1tYjMtRUNPU1lTVEVNIiwidyI6W3siZm4iOiJlbnZmcXFlMWF5NGsxLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.zabUOXjrjECF0vX7OToXxH6fxwW0rINfDP5-u9XLJoI/image;s=184x138;q=80', 


"""