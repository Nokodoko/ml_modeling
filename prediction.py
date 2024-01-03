#!/bin/env python3
from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
import pandas as pd

# CONSTANTS
file = './melb_data.csv'
data = pd.read_csv(file)
base = data.dropna(axis=0)


def y(attr):  # PREDICTION
    y = base[attr]
    return y


# UPDATE PREDICTION HERE
prediction_feature = 'Price'

features = ['Landsize', 'Car',
            'Bedroom2', 'Postcode', 'Propertycount']

X = base[features]

tr_X, val_X, tr_y, val_y = train_test_split(
    X, y(prediction_feature), random_state=0)

val_base_model = DecisionTreeRegressor()
val_base_model.fit(tr_X, tr_y)
val_predictions = val_base_model.predict(val_X)
val_mae = mean_absolute_error(val_y, val_predictions)
print(f"Validation Predictions MAE: {val_mae}")

base_model = DecisionTreeRegressor(random_state=0)
base_model.fit(X, y(prediction_feature))
predictions = base_model.predict(X.head())
print(f"Top 5 predictions:{predictions}")


predicted_prices = base_model.predict(X)
mae = mean_absolute_error(y(prediction_feature), predicted_prices)
print(f"MAE/in sample score: {mae}")
