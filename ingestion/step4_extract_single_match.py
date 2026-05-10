import requests
import json
from step1_extract_events import my_api_key # Grab your key

# 1. HARDCODED v1 endpoint for a specific match
test_endpoint = "https://api.henrikdev.xyz/valorant/v2/esports/vlr/matches/644709"

req_headers = {"Authorization": my_api_key}

# 2. Simple GET request
response = requests.get(test_endpoint, headers=req_headers)

# 3. Simple Save
if response.status_code == 200:
    print("API request successful! Saving single match data...")
    with open('single_match_test.json', 'w') as file:
        json.dump(response.json(), file)
else:
    print(f"Failed! Status code: {response.status_code}")