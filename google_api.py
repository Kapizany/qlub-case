import os
import time
from xml.dom import ValidationErr
from dotenv import load_dotenv
import requests
import json

load_dotenv() 
api_key = os.environ.get("API_KEY", '')

def find_restaurant_by_city(city):
    if not api_key:
        raise ValidationErr("API key not found!", 401)
    results = []
    next_page_token = ''
    for time_sleep in [2,2,0]:
        url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={city}&type=restaurant&key={api_key}"
        if next_page_token:
            url += f"&pagetoken={next_page_token}"
        response = requests.get(url)
        res = json.loads(response.text)
        results += res["results"]
        if not res.get('next_page_token',''):
            break
        else:
            next_page_token = res['next_page_token']
            time.sleep(time_sleep)
    if not results:
        raise ValidationErr("No restaurant found!", 400)
    return results