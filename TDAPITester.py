import requests
import json
import os
import time
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from config import client_id,access_token,dir


def sell_share(share_price, num_shares, balance):
    balance += (num_shares * share_price)
    return balance

def buy_share(share_price, balance):
    num_shares = 0
    while (True):
        if (balance - share_price >= 0):
            num_shares += 1
            balance -= share_price
        else:
            break
    return num_shares, balance


#today's date and one week ago in epoch seconds for API request
today = time.time()
one_year_ago = today - 31556926

desiredStockTickers = ['PTON', 'AAPL', 'AMD', 'ZM', 'U', 'OSTK', 'FB']

#sample stock ticker


#curl call to get acc info from TD
os.system(f'curl -X GET --header "Authorization: Bearer {access_token}" "https://api.tdameritrade.com/v1/accounts/454199960?fields=positions" > {dir}/stockbot/accBalance.json')

for desiredStockTicker in desiredStockTickers:
#curl call to get YTD stock info on a given stock
    #os.system(f'curl -X GET --header "Authorization: Bearer {access_token}" "https://api.tdameritrade.com/v1/marketdata/{desiredStockTicker}/pricehistory?apikey={client_id}&periodType=ytd&frequencyType=daily&frequency=1&needExtendedHoursData=true" > {dir}/stockbot/priceHistory{desiredStockTicker}.json')

    #curl call to get day stock info on a given stock
    #os.system(f'curl -X GET --header "Authorization: Bearer {access_token}" "https://api.tdameritrade.com/v1/marketdata/{desiredStockTicker}/pricehistory?apikey={client_id}&periodType=day&frequencyType=minute&frequency=10&needExtendedHoursData=true" > {dir}/stockbot/dayHistory.json')

    ticker_history_path = f'C:\\Users\\LennyRogan\\Documents\\Python\\stockbot\\priceHistory{desiredStockTicker}.json'
    df = pd.DataFrame(columns = ['open','high','low','close','volume','datetime'])
    for _dict in pd.read_json(ticker_history_path).iloc[:,0]:
        df = df.append(_dict,ignore_index=True)

    #print(df)
    #print(index)
    #print(df)
    df['SMA5'  ] = df.iloc[:,1].rolling(window=5  ).mean()
    df['SMA10' ] = df.iloc[:,1].rolling(window=10 ).mean()
    df['SMA50' ] = df.iloc[:,1].rolling(window=50 ).mean()
    df['SMA200'] = df.iloc[:,1].rolling(window=200).mean()

    #print(df)

    # plt.title(f'{desiredStockTicker}')
    # plt.plot(df['high'  ], label='high')
    # plt.plot(df['SMA5'  ], label='SMA5')
    # plt.plot(df['SMA10' ], label='SMA10')
    # plt.plot(df['SMA50' ], label='SMA50')
    # #plt.plot(df['SMA200'], label='SMA200')
    # plt.legend(loc=2)
    # plt.savefig(f'{desiredStockTicker}_data.svg', format='svg', dpi = 1200)
    # plt.clf()

    num_shares = 0
    balance = 100000
    own_shares = False
    share_high = 0

    for i in range (10,len(df.iloc[:,8])):
        if (own_shares):
            if (df.iloc[:,3][i] > share_high):
                share_high = df.iloc[:,3][i]
            elif (df.iloc[:,3][i] <= share_high * .98):
                balance = sell_share(df.iloc[:,3][i], num_shares, balance)
                own_shares = False
                print(f"Sell at {df.iloc[:,3][i]}")
            # if (df.iloc[:,7][i] <= df.iloc[:,8][i]):
            #     balance = sell_share(df.iloc[:,3][i], num_shares, balance)
            #     own_shares = False
            #     print(f"Sell at {df.iloc[:,3][i]}")
        else:
            if df.iloc[:,7][i] >= df.iloc[:,8][i]:
                num_shares, balance = buy_share(df.iloc[:,3][i], balance)
                own_shares = True
                print(f"Buy at {df.iloc[:,3][i]}")
                share_high = df.iloc[:,3][i]
    balance = sell_share(df.iloc[:,3][len(df.iloc[:,8]) - 1], num_shares, balance)
    print (balance)
    percent_profit = (balance / 100000)*100
    print (f"percent profit on {desiredStockTicker}: {percent_profit}")



