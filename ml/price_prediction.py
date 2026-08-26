import pandas as pd
import joblib
import numpy as np

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def predict_price(model, x):
    prediction = model.predict(x)
    return prediction


def encode_market_data(data):
    data = data.copy()

    data["crop"] = data["crop"].astype("category").cat.codes
    data["location"] = data["location"].astype("category").cat.codes
    data["quality"] = data["quality"].astype("category").cat.codes

    return data


def train_price_model():
    data = pd.read_csv("ml/market_price_data.csv")

    encoded_data = encode_market_data(data)

    X = encoded_data[
        ["crop", "location", "quality", "quantity"]
    ]

    y = encoded_data["market_price"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, predictions)

    print("Model trained successfully")
    print("Mean Absolute Error (MAE):", mae)
    print("Mean Squared Error (MSE):", mse)
    print("Root Mean Squared Error (RMSE):", rmse)
    print("R2 Score:", r2)

    joblib.dump(model, "ml/price_model.pkl")

    print("Model saved as ml/price_model.pkl")

    return model


def load_price_model():
    return joblib.load("ml/price_model.pkl")


if __name__ == "__main__":
    train_price_model()
    

