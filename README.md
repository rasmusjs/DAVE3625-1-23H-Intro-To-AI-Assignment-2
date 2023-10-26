# Assignment 2: Machine Learning - Documentation

You have 10 days to work on a machine learning algorithm.
I want you to pick one of the following use cases and make a prediction algorithm using either regression or
classification algorithms.

Do the following:

1. Pick one use case (defined below).
2. Explore and research which algorithm would work best for this use case (regression or classification)
3. Document your findings in a file (3-5 lines) on why you chose this algorithm.
4. Train the algorithm using Python
5. Keep the solution as simple as possible. We are not looking for the best machine learning algorithm. We are
   interested in seeing that you know how to work with machine learning.
6. Publish the code on GitHub and send us the link

You can pick one of the following use cases:

1. Predict stock market price for TESLA.
   I want you to make a prediction algorithm which predicts the price of this stock on a specific date. Input will be
   date and output should be price of that stock (close value in the data file).
   You should also show the prediction percentage score.
   Data file: TESLA.csv
   For updated csv file, please download the data from:
   https://finance.yahoo.com/quote/TSLA/history?p=TSLA

We picked the stock predicting use case for TESLA, mainly because finance is a hobby of some of us. We chose regression
algorithm because it matched our data best, since the data is continuous and not discrete. For predicting stock
prices we first tried to use a polynomial regression algorithm with many degrees (6) but the mean squared error was
really high, at over 500. Then we found a article why Autoregressive Integrated Moving Average was better for our spikey
data, since we are using time series (Dhaduk, 2021). Some of the code is based on a "Time Series Analysis: ARIMA Models
in Python".

Source:

Dhaduk, Hardikkumar, 2021
Stock market forecasting using Time Series analysis With ARIMA model
https://www.analyticsvidhya.com/blog/2021/07/stock-market-forecasting-using-time-series-analysis-with-arima-model/

Awan, Abid Ali, 2023
Time Series Analysis: ARIMA Models in Python
https://www.kdnuggets.com/2023/08/times-series-analysis-arima-models-python.html