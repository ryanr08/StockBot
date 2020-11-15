#Double Moving Average Crossover

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import csv
# with open ("./AAPL_daily_adj.csv", "w") as file:
#     with open('./Data/training_data/AAPL_daily_adj.csv', 'r') as textfile:
#         for row in reversed(list(csv.reader(textfile))):
#             file.write(', '.join(row))
#             file.write('\n')
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

def main():
    AAPL_daily = pd.read_csv("./AAPL_daily_adj.csv")
    AAPL_SMA50 = pd.read_csv("./Data/training_data/AAPL_sma50.csv")
    AAPL_SMA200 = pd.read_csv("./Data/training_data/AAPL_sma200.csv")
    AAPL_SMA30 = pd.read_csv("./Data/training_data/AAPL_sma30.csv")
    AAPL_SMA100 = pd.read_csv("./Data/training_data/AAPL_sma100.csv")

    plt.figure(figsize=(20, 10))
    plt.plot(AAPL_daily[' 5. adjusted close'], label='AAPL', color='green')
    plt.plot(AAPL_SMA50['SMA'], label='SMA50', color='blue')
    plt.plot(AAPL_SMA200['SMA'], label='SMA200', color='red')
    plt.plot(AAPL_SMA30['SMA'], label='SMA30', color='yellow')
    plt.plot(AAPL_SMA100['SMA'], label='SMA100', color='purple')
    plt.ylabel('Apple adj prices & SMAs')
    plt.xlabel('1999 - 2020')
    plt.legend(loc='upper left')
    plt.title("Apple close prices and SMAs over time")
    #plt.savefig("plt.png")

    num_shares = 0
    balance = 100000
    own_shares = False
    share_high = -1
    for i in range (5200, len(AAPL_daily.iloc[:,5])):
        if (own_shares):
            if (AAPL_daily.iloc[:,5][i] > share_high):
                share_high = AAPL_daily.iloc[:,5][i]
            elif (AAPL_daily.iloc[:,5][i] <= share_high * .80):
                balance = sell_share(AAPL_daily.iloc[:,5][i], num_shares, balance)
                own_shares = False
                share_high = 0
                print(f"Sell at: {AAPL_daily.iloc[:,5][i]}")
            elif (AAPL_SMA30.iloc[:,1][i - 30] <= AAPL_SMA200.iloc[:,1][i - 200]):
                balance = sell_share(AAPL_daily.iloc[:,5][i], num_shares, balance)
                own_shares = False
                share_high = 0
                print(f"Sell at: {AAPL_daily.iloc[:,5][i]}")
        else:
            if (AAPL_SMA30.iloc[:,1][i - 30] >= AAPL_SMA200.iloc[:,1][i - 200]):
                num_shares, balance = buy_share(AAPL_daily.iloc[:,5][i], balance)
                own_shares = True
                print(f"Buy at: {AAPL_daily.iloc[:,5][i]}")
                share_high = AAPL_daily.iloc[:,5][i]
    balance = sell_share(AAPL_daily.iloc[:,5][len(AAPL_daily.iloc[:,5]) - 1], num_shares, balance)
    print (balance)
    percent_profit = balance / 100000
    print (f"percent profit: {percent_profit}")

if __name__ == '__main__':
    main()