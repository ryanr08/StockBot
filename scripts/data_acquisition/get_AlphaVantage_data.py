from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
import json
import argparse


def save_dataset(symbol, time_window):
    api_key = ""
    with open("./api_key.txt") as file:
        reader = file.read()
        api_key = reader
    print(symbol, time_window)
    ts = TimeSeries(key=api_key, output_format='pandas')
    if time_window == 'intraday':
        data, meta_data = ts.get_intraday(
            symbol, interval='1min', outputsize='full')
    elif time_window == 'daily':
        data, meta_data = ts.get_daily(symbol, outputsize='full')
    elif time_window == 'daily_adj':
        data, meta_data = ts.get_daily_adjusted(symbol, outputsize='full')
    elif time_window == 'monthly':
        data, meta_data = ts.get_monthly(symbol)

    pprint(data.head(10))

    data.to_csv(f'../../Data/training_data/{symbol}_{time_window}.csv')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('symbol', type=str, help="the stock symbol you want to download")
    parser.add_argument('time_window', type=str, choices=[
                        'intraday', 'daily', 'daily_adj', 'monthly'], help="the time period you want to download the stock history for")

    namespace = parser.parse_args()
    save_dataset(**vars(namespace))