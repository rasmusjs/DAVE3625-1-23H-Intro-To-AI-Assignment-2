import pickle
import sys

import pandas as pd

# Path to model and dataset
model = "TSLA-ARIMA-2018.sav"

# Load the dataset to get the first date and the actual closing price of that day
df = pd.read_csv("data/TSLA-2018.csv", parse_dates=True)

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

# Count the number of days between the input date and the first
count_days = abs(int((date - min_date).days))

# Predict the closing price
predicted_close = model_fit.predict(start=count_days, end=count_days)[0]

# Convert the date to a string, used for prettier printing. (YYYY-MM-DD) and no timestamp
date = str(date.date())
print()  # Newline

# If the date is in the dataset we can compare the predicted closing price with the actual closing price
if count_days < len(df):

    # Get the actual closing price
    actual_close = df.loc[count_days, "Close"]

    # Calculate the accuracy of the prediction
    if actual_close < predicted_close:  # If the predicted closing price this will be the numerator
        percent = round((actual_close / predicted_close) * 100, 2)
    else:
        percent = round((predicted_close / actual_close) * 100, 2)

    # Print the predicted closing price
    print(f"Predicted Close for {date}: {round(predicted_close, 2)} USD")
    print(f"Actual price {round(actual_close, 2)} USD")
    print(f"Accuracy: {percent}%")
else:
    print(f"Predicted Close for {date}: {round(predicted_close, 2)} USD")

sys.exit()
