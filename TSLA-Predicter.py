import pickle
import sys

import pandas as pd

# Path to model and dataset
model = "TSLA-ARIMA-2018.sav"

# Load the dataset to get the first date and the actual closing price of that day
df = pd.read_csv("data/TSLA-2018.csv")

# Convert the date column to a datetime object
df['Date'] = pd.to_datetime(df['Date'])

# Find the first date in the dataset, used to calculate days.
min_date = pd.to_datetime(df["Date"].min())

# Load the trained model
model = pickle.load(open(model, 'rb'))

# Fit the model (needed for arima.predict())
model_fit = model.fit()

# Input a date a date and convert it to a datetime object
try:
    date = pd.to_datetime(input(f"Input a date YYYY-MM-DD: "))
except KeyboardInterrupt:
    print("\nExiting...")
    exit()
except ValueError:
    print("Please input a valid date in the format YYYY-MM-DD")
    exit()

# Variable to count the days between the first date in the dataset and the input date
count_days = 0

# Try to find the date in the dataset that is closest to the input date
for i in range(len(df)):
    if date == df.loc[i, "Date"]:  # Break if exact match
        break
    elif date < df.loc[i, "Date"]:  # Break if higher than input date
        break
    count_days += 1

# Predict the closing price
predicted_close = model_fit.predict(start=count_days, end=count_days)[0]

# Convert the date to a string, used for prettier printing. (YYYY-MM-DD) and no timestamp
date = str(date.date())
print()  # Newline

# If the date is in the dataset we can compare the predicted closing price with the actual closing price
if count_days < len(df):

    # Get the actual value from dataset
    real_value = df.loc[count_days]
    actual_date, actual_close = real_value["Date"], real_value["Close"]

    # Calculate the accuracy of the prediction
    if actual_close < predicted_close:  # If the predicted closing price this will be the numerator
        percent = round((actual_close / predicted_close) * 100, 2)
    else:
        percent = round((predicted_close / actual_close) * 100, 2)

    # Print the predicted closing price
    print(f"Predicted close for {date}: {round(predicted_close, 2)} USD")
    print(f"Actual price {actual_date}: {round(actual_close, 2)} USD")
    print(f"Prediction accuracy: {percent}%")
else:
    print(f"Predicted close for {date}: {round(predicted_close, 2)} USD")

sys.exit()
