#!/bin/env python3
from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
import pandas as pd

# CONSTANTS
FILE = './melb_data.csv'
DATA = pd.read_csv(FILE)
BASE = DATA.dropna(axis=0)


def Y(attr):
    return BASE[attr]


# UPDATE PREDICTION HERE
prediction_feature = 'Price'

features = [
    'Landsize',
    'Car',
    'Bedroom2',
    'Postcode',
    'Propertycount'
]

X = BASE[features]

tr_X, val_X, tr_y, val_y = train_test_split(
    X, Y(prediction_feature), random_state=0)

val_base_model = DecisionTreeRegressor()
val_base_model.fit(tr_X, tr_y)
val_predictions = val_base_model.predict(val_X)
val_mae = mean_absolute_error(val_y, val_predictions)
print(f"Validation Predictions MAE: {val_mae}")

base_model = DecisionTreeRegressor(random_state=0)
base_model.fit(X, Y(prediction_feature))
predictions = base_model.predict(X.head())
print(f"Top 5 predictions:{predictions}")


predicted_prices = base_model.predict(X)


def get_mae(max_leaf_nodes, train_X, value_X, train_Y, value_Y):
    model = DecisionTreeRegressor(
        max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_Y)
    predictions = model.predict(value_X)
    mae = mean_absolute_error(value_Y, predictions)
    return mae


def get_best_leaf(leaf_array):
    scores = {leaf_size: get_mae(
        leaf_size, tr_X, val_X, tr_y, val_y) for leaf_size in leaf_array}
    best_score = min(scores, key=scores.get)
    best_mae = scores[best_score]
    print(f"Best Leaf Size: {best_score} \t\t MAE: {best_mae}")


leaf_nodes_list = [5, 50, 500, 5000]

get_best_leaf(leaf_nodes_list)
