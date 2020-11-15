import requests
import json
import os
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from config import client_id,access_token,dir

#today's date and one week ago in epoch seconds for API request
today = time.time()
one_year_ago = today - 31556926

desiredStockTickers = ['PTON', 'AAPL', 'AMD', 'ZM', 'U', 'OSTK', 'FB']

#sample stock ticker


#curl call to get acc info from TD
#os.system(f'curl -X GET --header "Authorization: Bearer {access_token}" "https://api.tdameritrade.com/v1/accounts/454199960?fields=positions"')

for desiredStockTicker in desiredStockTickers:
#curl call to get YTD stock info on a given stock
    os.system(f'curl -X GET --header "Authorization: Bearer {access_token}" "https://api.tdameritrade.com/v1/marketdata/{desiredStockTicker}/pricehistory?apikey={client_id}&periodType=ytd&frequencyType=daily&frequency=1&needExtendedHoursData=true" > {dir}/stockbot/priceHistory{desiredStockTicker}.json')

    #curl call to get day stock info on a given stock
    #os.system(f'curl -X GET --header "Authorization: Bearer {access_token}" "https://api.tdameritrade.com/v1/marketdata/{desiredStockTicker}/pricehistory?apikey={client_id}&periodType=day&frequencyType=minute&frequency=10&needExtendedHoursData=true" > {dir}/stockbot/dayHistory.json')

    ticker_history_path = f'C:\\Users\\LennyRogan\\Documents\\Python\\stockbot\\priceHistory{desiredStockTicker}.json'
    df = pd.DataFrame(columns = ['open','high','low','close','volume','datetime'])
    for _dict in pd.read_json(ticker_history_path).iloc[:,0]:
        df = df.append(_dict,ignore_index=True)

    print(df)
    #print(index)
    #print(df)
    df['SMA5'  ] = df.iloc[:,1].rolling(window=5  ).mean()
    df['SMA10' ] = df.iloc[:,1].rolling(window=10 ).mean()
    df['SMA50' ] = df.iloc[:,1].rolling(window=50 ).mean()
    df['SMA200'] = df.iloc[:,1].rolling(window=200).mean()

    print(df)

    plt.title(f'{desiredStockTicker}')
    plt.plot(df['high'  ], label='high')
    plt.plot(df['SMA5'  ], label='SMA5')
    plt.plot(df['SMA10' ], label='SMA10')
    plt.plot(df['SMA50' ], label='SMA50')
    #plt.plot(df['SMA200'], label='SMA200')
    plt.legend(loc=2)
    plt.savefig(f'{desiredStockTicker}_data.svg', format='svg', dpi = 1200)
    plt.clf()