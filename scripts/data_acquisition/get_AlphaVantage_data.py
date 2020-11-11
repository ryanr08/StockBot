from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
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
    ti = TechIndicators(key=api_key, output_format='pandas')
    if time_window == "sma":
        data, meta_data = ti.get_sma(symbol, interval="daily", time_period=50, series_type='close')
        pprint(data.head(10))
        data.to_csv(f'../../Data/training_data/{symbol}_sma50.csv')
        data, meta_data = ti.get_sma(symbol, interval="daily", time_period=200, series_type='close')
        pprint(data.head(10))
        data.to_csv(f'../../Data/training_data/{symbol}_sma200.csv')
        data, meta_data = ti.get_sma(symbol, interval="daily", time_period=100, series_type='close')
        pprint(data.head(10))
        data.to_csv(f'../../Data/training_data/{symbol}_sma100.csv')
        data, meta_data = ti.get_sma(symbol, interval="daily", time_period=30, series_type='close')
        pprint(data.head(10))
        data.to_csv(f'../../Data/training_data/{symbol}_sma30.csv')
    elif time_window == 'intraday':
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
    print("LOG")
    parser = argparse.ArgumentParser()

    parser.add_argument('symbol', type=str, help="the stock symbol you want to download")
    parser.add_argument('time_window', type=str, choices=[
                        'intraday', 'daily', 'daily_adj', 'monthly', "sma"], help="the time period you want to download the stock history for")
    #parser.add_argument ('SMA', type=bool, help="If true, will return 50 day SMA and 200 day SMA for given symbol.")

    namespace = parser.parse_args()
    save_dataset(**vars(namespace))