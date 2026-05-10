import json

def read_json_from_lake():
    with open ('json_files/raw_vct_events.json' , 'r') as file:
        vct_events = json.load(file)
        
        events_list = vct_events["data"]
        ids = []

        for event in events_list[:3]:
            ids.append(event["id"])

        return ids

tournament_ids = read_json_from_lake()