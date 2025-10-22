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

train_x, test_x, train_y, test_y = train_test_split(model_data[['Square_Footage']], model_data['House_Price'], random_state=50)

# check test and train size without giving test_size and train_size [Default Split 75% and 25%]
mean_of_x = model_data["Square_Footage"].mean()
mean_of_y = model_data["House_Price"].mean()
print("Mean of X", mean_of_x, "Mean of Y", mean_of_y)
numerator_sum = 0
denominator_sum = 0
for xi,yi in zip(model_data["Square_Footage"].values, model_data["House_Price"].values):
    numerator_sum += (xi - mean_of_x)*(yi - mean_of_y)
    denominator_sum += (xi - mean_of_x)**2

print("Numerator",numerator_sum,"Denominator",denominator_sum)

slope_m = numerator_sum/denominator_sum

print("Slope",slope_m)

intercept = mean_of_y - (slope_m*mean_of_x)
print("Intercept", intercept)



print(type(train_x))
print(train_x.shape)
print(train_y.shape)
print(test_x.shape)
print(test_y.shape)

#  training and testing set are maintained of the same index

print("++++++++++++++++++")
print(train_x)
print("++++++++++++++++++")
print(train_y)
print("++++++++++++++++++")
print(test_x)
print("++++++++++++++++++")
print(test_y)
print("++++++++++++++++++")

model = LinearRegression()
model.fit(train_x, train_y)
y_predict = model.predict(test_x)

print("Slope/Coefficient by Method:", model.coef_)
print("Intercept by Method:", model.intercept_)

print(mean_squared_error(test_y, y_predict))
print(root_mean_squared_error(test_y, y_predict))
print(r2_score(test_y, y_predict))

plt.figure()
plt.scatter(test_x, test_y, label="Data Points")
plt.plot(test_x, y_predict, color="yellow", label="Regression Line")
plt.legend()
plt.title("Linear Regression of Square Footage and House Price")
plt.xlabel("Square Footage")
plt.ylabel("House Price")
plt.legend()
plt.grid(True)
plt.show()