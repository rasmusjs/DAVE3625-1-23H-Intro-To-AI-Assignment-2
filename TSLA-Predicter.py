import pickle

filename = "TSLA.cc"
loaded_model = pickle.load(open(filename, 'rb'))

# Taking integer input from user
num = int(input("Enter number "))

for i in range(0, num):
    model_fit = loaded_model.fit()
    prediction = model_fit.forecast()[0]
    print(prediction)
