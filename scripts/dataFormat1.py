import pandas as pd
from sklearn import preprocessing
import numpy as np
import sys

history_points = 50

def csv_to_dataset(csv_path):
    data = pd.read_csv(csv_path)
    data = data.drop('date', axis=1)
    data = data.drop('Name',axis=1)
    data = data.drop('Unnamed: 7', axis=1)
    data = data.drop(0, axis=0)

    data_normaliser = preprocessing.MinMaxScaler()
    data_normalised = data_normaliser.fit_transform(data)


    # using the last {history_points} open close high low volume data points, predict the next open value
    ohlcv_histories_normalised = np.array([data_normalised[i:i + history_points].copy() for i in range(len(data_normalised) - history_points)])     # x parameter for training neural net
    next_day_open_values_normalised = np.array([data_normalised[:, 3][i + history_points].copy() for i in range(len(data_normalised) - history_points)])    # value we are trying to predict
    next_day_open_values_normalised = np.expand_dims(next_day_open_values_normalised, -1)

    next_day_open_values = np.array([data.iloc[:, 3][i + history_points].copy() for i in range(len(data) - history_points)])
    next_day_open_values = np.expand_dims(next_day_open_values, -1)

    y_normaliser = preprocessing.MinMaxScaler()
    y_normaliser.fit(next_day_open_values)

    assert ohlcv_histories_normalised.shape[0] == next_day_open_values_normalised.shape[0]
    return ohlcv_histories_normalised, next_day_open_values_normalised, next_day_open_values, y_normaliser

# get testing and training data prepared for a nueral net
def getDataset(csv_file):
    ohlcv_histories, next_day_open_values, unscaled_y, y_normaliser = csv_to_dataset(csv_file)

    test_split = 0.9 # the percent of data to be used for testing
    n = int(ohlcv_histories.shape[0] * test_split)

    # splitting the dataset up into train and test sets

    x_train = ohlcv_histories[:n]
    y_train = next_day_open_values[:n]

    x_test = ohlcv_histories[n:]
    y_test = next_day_open_values[n:]

    unscaled_y_test = unscaled_y[n:]

    return x_train, y_train, x_test, y_test, unscaled_y_test, ohlcv_histories, y_normaliser