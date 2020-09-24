import numpy as np
import sys
import os
import pandas as pd
import pprint
from sklearn import preprocessing
from tensorflow.keras.models import load_model
from dataFormat1 import history_points
from dataFormat1 import getDataset
from dataFormat1 import csv_to_dataset

symbol = ""

if (len(sys.argv) != 2):
    print("ERROR: script must have symbol as first and only argument")
    quit()
else:
    symbol = sys.argv[1]

data = pd.read_csv(f"../Data/training_data/{symbol}_test.csv")

pp = pprint.PrettyPrinter(indent = 4)
pp.pprint(data)

data = data.drop('date', axis=1)
data = data.drop('Unnamed: 6', axis=1)

pp.pprint(data)

data_normaliser = preprocessing.MinMaxScaler()
data_normalised = data_normaliser.fit_transform(data)
x_test = np.array([data_normalised[0:history_points].copy()])

next_day_open_values = np.array([data.iloc[:, 3][history_points - 1].copy()])
next_day_open_values = np.expand_dims(next_day_open_values, -1)

y_normaliser = preprocessing.MinMaxScaler()
y_normaliser.fit(next_day_open_values)

os.chdir('./models')
model = load_model(f'basic_model_{symbol}.h5')


y_test_predicted = model.predict(x_test)
y_test_predicted = y_normaliser.inverse_transform(y_test_predicted)

os.chdir('..')
with open("predictions.txt", 'a') as file:
    file.write(f"{symbol}: {y_test_predicted} \n")

# buys = []
# sells = []
# thresh = 0.1

# start = 0
# end = -1

# x = -1
# for ohlcv, ind in zip(ohlcv_test[start: end], tech_ind_test[start: end]):
#     normalised_price_today = ohlcv[-1][0]
#     normalised_price_today = np.array([[normalised_price_today]])
#     price_today = y_normaliser.inverse_transform(normalised_price_today)
#     predicted_price_tomorrow = np.squeeze(y_normaliser.inverse_transform(model.predict([[ohlcv], [ind]])))
#     delta = predicted_price_tomorrow - price_today
#     if delta > thresh:
#         buys.append((x, price_today[0][0]))
#     elif delta < -thresh:
#         sells.append((x, price_today[0][0]))
#     x += 1
# print(f"buys: {len(buys)}")
# print(f"sells: {len(sells)}")


# def compute_earnings(buys_, sells_):
#     purchase_amt = 10
#     stock = 0
#     balance = 0
#     while len(buys_) > 0 and len(sells_) > 0:
#         if buys_[0][0] < sells_[0][0]:
#             # time to buy $10 worth of stock
#             balance -= purchase_amt
#             stock += purchase_amt / buys_[0][1]
#             buys_.pop(0)
#         else:
#             # time to sell all of our stock
#             balance += stock * sells_[0][1]
#             stock = 0
#             sells_.pop(0)
#     print(f"earnings: ${balance}")


# # we create new lists so we dont modify the original
# compute_earnings([b for b in buys], [s for s in sells])

# import matplotlib.pyplot as plt

# plt.gcf().set_size_inches(22, 15, forward=True)

# real = plt.plot(unscaled_y_test[start:end], label='real')
# pred = plt.plot(y_test_predicted[start:end], label='predicted')

# if len(buys) > 0:
#     plt.scatter(list(list(zip(*buys))[0]), list(list(zip(*buys))[1]), c='#00ff00', s=50)
# if len(sells) > 0:
#     plt.scatter(list(list(zip(*sells))[0]), list(list(zip(*sells))[1]), c='#ff0000', s=50)

# # real = plt.plot(unscaled_y[start:end], label='real')
# # pred = plt.plot(y_predicted[start:end], label='predicted')

# plt.legend(['Real', 'Predicted', 'Buy', 'Sell'])

# plt.show()