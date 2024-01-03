#!/bin/env python3
from sklearn.tree import DecisionTreeRegressor
import pandas as pd

file = './melb_data.csv'

train = pd.read_csv(file)
data = train.describe()

print(data.T)
print(data)
# lot_area = data.columns.get_loc('LotArea')
#
# mean = data.index.get_loc('mean')
# std = data.index.get_loc('std')
#
# lot_area_mean = data.iloc[mean, lot_area]
# lot_area_std = data.iloc[std, lot_area]

# print(f"lot_area mean: {lot_area_mean}")
# print(f"lot_area std: {lot_area_std}")
# print(data.LotArea)

# melborne_data = data.dropna(axis=0)
# y = melborne_data.Price
# melborne_features = ['Rooms', 'Bathroom',
#                     'Landsize', 'Lattitude', 'Longtitude']
# X = melborne_data[melborne_features]
# X.describe()
#
# melborne_model = DecisionTreeRegressor(random_state=1)
# melborne_model.fit(X, y)
#
# print("predicting the next 5 houses:")
# print(X.head())
# print("Predictions are:")
# print(melborne_model.predict(X.head()))
