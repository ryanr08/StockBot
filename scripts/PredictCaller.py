import os
import json


list_of_tickers = list()

with open('constituents_json.json','r') as f:
    json_file = json.loads(f.read())
    
    for item in json_file:
        list_of_tickers.append(item["Symbol"])

for item in list_of_tickers:
    os.system(f"python predict.py {item}")