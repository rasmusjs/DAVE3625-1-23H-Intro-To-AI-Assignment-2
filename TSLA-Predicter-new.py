import pickle
import pandas as pd

# Paths to model and polynomial features
model = "model.sav"
polynomial_features = "poly.sav"

# Load the trained model and the polynomial features used to train the model
model, polynomial_features = pickle.load(open(model, 'rb')), pickle.load(open(polynomial_features, 'rb'))

# Input a date a date and convert it to a datetime object
try:
    date = pd.to_datetime(input(f"Input a date YYYY-MM-DD: "))
except ValueError:
    print("Please input a valid date in the format YYYY-MM-DD")
    exit()

# Create a dataframe with the input date
df = pd.DataFrame({'Date': [date]})

# Transform the input date using the same polynomial features used to train the model
x_poly_input = polynomial_features.transform(df)

# Predict the closing price for the input date using the loaded model
predicted_close = round(model.predict(x_poly_input)[0][0], 2)

# Print the predicted closing price
print(f"Predicted Close for {date}: {predicted_close} USD")
