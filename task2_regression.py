import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("house_data.csv")

# Features and target
X = df[["area", "bedrooms"]]
y = df["price"]

# Model
model = LinearRegression()
model.fit(X, y)

# Predictions
predictions = model.predict(X)

print("Predicted Prices:\n", predictions)

# Plot (area vs price)
plt.scatter(df["area"], df["price"])
plt.plot(df["area"], predictions)
plt.title("House Price Prediction")
plt.xlabel("Area")
plt.ylabel("Price")
plt.show()