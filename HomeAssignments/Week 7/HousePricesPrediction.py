import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, root_mean_squared_error
from sklearn.linear_model import LinearRegression

data = pd.read_csv(r"HomeAssignments\Week 7\house_price_regression_dataset.csv")
print(data)
print(data.isna().sum())
print(data.isnull().sum())
model_data = data[['Square_Footage','House_Price']]
print(model_data.head(10))
print(model_data.isna().sum())
print(model_data.isnull().sum())
print((data==0).sum()) # if we want to check sum of 0 in the records (what ever is true can be added)
plt.scatter(model_data['Square_Footage'],model_data['House_Price'])

train_x, test_x, train_y, test_y = train_test_split(model_data[['Square_Footage']], model_data['House_Price'])

model = LinearRegression()
model.fit(train_x, train_y)
y_predict = model.predict(test_x)
print(mean_squared_error(test_y, y_predict))
print(root_mean_squared_error(test_y, y_predict))
print(r2_score(test_y, y_predict))

plt.figure()
plt.scatter(test_x, test_y)
plt.plot(test_x, y_predict)
plt.show()