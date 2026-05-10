import requests
import time
import json
from step1_extract_events import my_api_key
from step2_extract_ids import read_json_from_lake

tournament_ids = read_json_from_lake()

def read_from_matches_api():
    match_data = {}
    for id in tournament_ids:
        matches_endpoint = f"https://api.henrikdev.xyz//valorant/v2/esports/vlr/events/{id}/matches"
        req_headers = {"Authorization" : my_api_key}
        response = requests.get(matches_endpoint, headers=req_headers)

        if response.status_code == 200:
            print("API request successful")
            print(f"Successfully fetched matches for tournament {id}")
            match_data[id] = response.json()
        elif response.status_code == 404:
            raise Exception("API endpoint not found (404)")
        elif response.status_code == 429:
            raise Exception("API rate limit reached(429). We might neeed to slow down our requests.")
        else:
            raise Exception(f"API request failed with status code {response.status_code}")
        
        time.sleep(5)
    return match_data

matches = read_from_matches_api()

with open('json_files/raw_vct_matches.json','w') as file:
    json.dump(matches, file)