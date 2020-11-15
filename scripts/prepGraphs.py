import csv
import os

os.chdir(r'C:\Users\LennyRogan\Documents\Python\stockbot\StockBot\scripts')

tickers_and_prices = {}

with open('predictions.txt', 'r') as txtfile:
    for line in txtfile:
        line_ = line.strip()
        ticker = line_[:line_.find(':')]
        predicted_price = line_[line_.find('[[')+2:line_.find(']]')]
        tickers_and_prices[ticker] = {}
        tickers_and_prices[ticker]['Ticker'] = ticker
        tickers_and_prices[ticker]['Predicted Close'] = predicted_price

print(tickers_and_prices)

os.chdir('./split_5_year_data')
print(os.getcwd())

for ticker in tickers_and_prices.values():
    try:
        with open(f"{ticker['Ticker']}_for_predicting.txt", 'r') as predictfile:
                real_price = predictfile.read()
                ticker['Real Close'] = real_price
    except(FileNotFoundError):
        print(f"{ticker['Ticker']} does not have historical data / modeling. Moving on... ")
    try:
        with open(f"{ticker['Ticker']}_test.csv", 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for line in reader:
                    if line['date'] == '2018-02-06':
                        dayBefore = line['close']
                        break
                ticker['Yesterday\'s Close'] = dayBefore 
    except(FileNotFoundError):
        print(f"{ticker['Ticker']} does not have historical data. Moving on ... ")
    ticker['Real Increase'] = float(ticker['Real Close'])-float(ticker['Yesterday\'s Close'])
    ticker['Predicted Increase'] = float(ticker['Predicted Close'])-float(ticker['Yesterday\'s Close'])
    ticker['Real Percentage Increase'] = ticker['Real Increase'] / float(ticker['Yesterday\'s Close'])
    ticker['Predicted Percentage Increase'] = ticker['Predicted Increase'] / float(ticker['Yesterday\'s Close'])
    ticker['Real Minus Predicted Percentage'] = ticker['Real Percentage Increase'] - ticker['Predicted Percentage Increase']
    
os.chdir('..')
with open('Accuracy_Measurements.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile,['Ticker','Predicted Close','Real Close','Yesterday\'s Close','Real Increase','Predicted Increase','Real Percentage Increase','Predicted Percentage Increase','Real Minus Predicted Percentage']) 
    writer.writeheader()
    for ticker in tickers_and_prices.values():
        writer.writerow(ticker)

       

print("""


""")

print(tickers_and_prices)

