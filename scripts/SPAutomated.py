import csv
import os
import sys
import json

#

init_dir = os.getcwd()
print(init_dir)
list_of_tickers = list()


with open('constituents_json.json','r') as f:
    json_file = json.loads(f.read())
    
    for item in json_file:
        list_of_tickers.append(item["Symbol"])

print(list_of_tickers)
print(len(list_of_tickers))


for item in list_of_tickers:
    print(init_dir)
    # os.chdir(init_dir + '/data_acquisition/')
    # os.system(f"python get_AlphaVantage_data.py {item} daily")

    os.chdir("..")
    # csvLocation = f"../Data/training_data/{item}_daily.csv"
    # os.system(f"python basic_model.py {csvLocation} {item}")

    linesForTesting = list()
    print(os.getcwd())
    os.chdir(os.getcwd())
    os.chdir("./Data/training_data")
    with open(f"{item}_daily.csv", 'r') as file:
        reader = csv.reader(file)
        linesForTesting = list(reader)
    with open(f"{item}_test.csv", 'w') as file:
        lineCount = 0
        for item in linesForTesting:
            if lineCount < 51:
                for line in item:
                    file.write(line + ',')
                file.write("\n")
                lineCount += 1
    os.chdir(init_dir)
    #os.system(f'python predict.py {item}')

                

