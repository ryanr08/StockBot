import csv
import json
import os 

list_of_tickers = list()

os.chdir(r'C:\Users\LennyRogan\Documents\Python\stockbot\StockBot\scripts')

def find_nth(s, x, n=0, overlap=False):
    l = 1 if overlap else len(x)
    i = -l
    for c in range(n + 1):
        i = s.find(x, i + l)
        if i < 0:
            break
    return i

with open('constituents_json.json','r') as f:
    json_file = json.loads(f.read())
    
    for item in json_file:
        list_of_tickers.append(item["Symbol"])

print(list_of_tickers)


with open('all_stocks_5yr.csv','r') as file:
    os.chdir('./split_5_year_data')
    reader = csv.DictReader(file)
    currSymbol = ''
    lines_for_writing = list()
    for line in reader:
        currSymbol = line['Name']
        if line['date'] != '2018-02-07':
            lines_for_writing.append(line)
        else:
            lines_for_training = list()
            with open(f'{currSymbol}_train.csv','w') as file2:
                for item in reader.fieldnames:
                        file2.write(item + ',')
                file2.write('\n')
                for i in range(len(lines_for_writing)):
                    line_ = lines_for_writing.pop()
                    if i < 50:
                        lines_for_training.append(line_)
                    for item in line_:
                        file2.write(line_[item] + ',')
                    file2.write('\n')
            with open(f'{currSymbol}_test.csv','w') as file2:
                for item in reader.fieldnames:
                        file2.write(item + ',')
                file2.write('\n')
                for line_ in lines_for_training:
                    for item in line_:
                        file2.write(line_[item] + ',')
                    file2.write('\n')
            lines_for_writing = list()
            with open(f'{currSymbol}_for_predicting.txt','w') as file2:
                count = 1
                for item in line.values():
                    if count == 5:
                        file2.write(item)
                        break
                    else:
                        count += 1
        
