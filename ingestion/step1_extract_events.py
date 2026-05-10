import requests
import json

events_endpoint = "https://api.henrikdev.xyz/valorant/v2/esports/vlr/events"
my_api_key = "HDEV-6e79f38e-441e-428b-bd92-4fe3737d2113"

def read_from_events_api(endpoint):
    

    req_headers = {
        "Authorization":  my_api_key
    }

    response = requests.get(endpoint, headers=req_headers)

    if response.status_code == 200:
        print("API request successful")
        return response.json()
    elif response.status_code == 404:
        raise Exception("API endpoint not found (404)")
    elif response.status_code == 429:
        raise Exception("API rate limit reached(429). We might neeed to slow down our requests.")
    else:
        raise Exception(f"API request failed with status code {response.status_code}")
    
events_data = read_from_events_api(events_endpoint)

with open('json_files/raw_vct_events.json', 'w') as file:
    json.dump(events_data, file)