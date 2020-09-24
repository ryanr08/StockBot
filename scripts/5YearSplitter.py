import csv
import json

list_of_tickers = list()

os.chdir('C:\Users\LennyRogan\Documents\Python\stockbot\StockBot\scripts')

with open('constituents_json.json','r') as f:
    json_file = json.loads(f.read())
    
    for item in json_file:
        list_of_tickers.append(item["Symbol"])

print(list_of_tickers)


with open('all_stocks_5yr.csv','r') as file:
    reader = csv.DictReader(file)
    currSymbol = ''
    lines_for_writing = list()
    for line in reader:
        currSymbol = line['Name']
        if line['date'] != '2/7/2018' and line['date'] != 'date':
            lines_for_writing.append()
        
