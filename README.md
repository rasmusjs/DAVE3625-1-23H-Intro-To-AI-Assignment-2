# Assignment 2: Machine Learning - Documentation

## Made by Ole Kristian Håseth Rudjord (s354564), Jørgen Skontorp (s364516) og Rasmus Skramstad (s360619)

Contents:
See main.ipynb for to documentation of the code used to train the model.
TSLA-Predicter.py is the program that uses the model to predict the stock price from a date given.

We picked the stock predicting use case, mainly because finance is a hobby of some of us. We chose a
regression algorithm because it matched our data best, since the data is continuous and not discrete. For predicting the
stock we used ARIMA (Auto-Regressive Integrated Moving Average) (Yugesh, 2021). The reason we chose ARIMA is that it is
ment for time series forecasting, and we wanted a challenge (Artley, 2022). The data we trained on is from 2018 to
October 29, 2023.

For running the predictor, run the program and follow the prompt. The program will ask for a date, and then it will use
the model to give a prediction on that valid date. If the date is in the dataset it will show you how off the prediction
is.

Sources:

Artley, Brendan, 2022

[Time Series Forecasting with ARIMA , SARIMA and SARIMAX](https://towardsdatascience.com/time-series-forecasting-with-arima-sarima-and-sarimax-ee61099e78f6)

Dhaduk, Hardikkumar, 2021
[Stock market forecasting using Time Series analysis With ARIMA model](https://www.analyticsvidhya.com/blog/2021/07/stock-market-forecasting-using-time-series-analysis-with-arima-model/)

Awan, Abid Ali, 2023
[Time Series Analysis: ARIMA Models in Python - KDnuggets](https://www.kdnuggets.com/2023/08/times-series-analysis-arima-models-python.html)

Verma, Yugesh, 2021

[Complete Guide To SARIMAX in Python for Time Series Modeling](https://analyticsindiamag.com/complete-guide-to-sarimax-in-python-for-time-series-modeling/)
