#!/bin/env python3

import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

file = 'melb_data.csv'
melb = pd.read_csv(file)

imputer = SimpleImputer(strategy='mean')


def y(attr):
    y = imputer.fit_transform(melb[[attr]]).ravel()
    return y


pred_feature = 'YearBuilt'
features = ["Rooms", "Price", "Distance", "Postcode", "Bedroom2", "Bathroom",
            "Car", "Landsize", "YearBuilt", "Lattitude", "Longtitude", "Propertycount"]


X = imputer.fit_transform(melb[features])

tr_x, val_x, tr_y, val_y = train_test_split(X, y(pred_feature), random_state=0)
valid_melb_model = DecisionTreeRegressor()
valid_melb_model.fit(tr_x, tr_y)
valid_predictions = valid_melb_model.predict(val_x)
valid_mae = mean_absolute_error(val_y, valid_predictions)
print(f"Predictions: {valid_predictions}")
print(f"Mean Absolute Error (moe): {valid_mae}")
