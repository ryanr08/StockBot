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
plt.savefig("plt.png")

#NEED to implement:
# every x minutes/hours every day:
    # grab intraday trading values
    # grab intraday SMAs
    # if SMA50 > SMA200:
        # buy stock at current price
    # if SMA50 < SMA200:
        # sell all shares of stock