import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np

def removing_outliers(df:pd.DataFrame, column_name):

    column_data = df[column_name]

    q3 = column_data.quantile(0.75)
    q1 = column_data.quantile(0.25)

    print("Q3", q3, "Q1", q1, "for", column_name)

    iqr = q3 - q1
    print("IQR", iqr, "for", column_name)

    lowerbound = q1 - (1.5*iqr)
    upperbound = q3 + (1.5*iqr)

    print("LowerBound", lowerbound, "for", column_name)
    print("UpperBound", upperbound, "for", column_name)

    non_outlier_data = df[(df[column_name]>=lowerbound) & (df[column_name]<=upperbound)]

    print("Removed Outlier", non_outlier_data)
    print("No of Records", non_outlier_data.shape)

    return non_outlier_data

df = pd.read_csv("HomeAssignments\Week 10\sales_data.csv")

df = removing_outliers(df, 'Total Amount')
df = removing_outliers(df, 'Advertising_Spend')

x = df[['Advertising_Spend']]
y = df['Total Amount']

poly_for_x = PolynomialFeatures(degree=2)
x_poly = poly_for_x.fit_transform(x)
print(poly_for_x)

x_train, x_test, y_train, y_test = train_test_split(x_poly, y, test_size=0.2, random_state=42)

# without polynomial features
x_l_train, x_l_test, y_l_train, y_l_test = train_test_split(x,y,test_size=0.2, random_state=42)

print(x_train)
print(x_test)
print(y_train)
print(y_test)

model = LinearRegression()
no_poly_model = LinearRegression()

plt.figure()
a = x_test[:, 1]
indices = np.argsort(a)
x_sorted = x_test[indices]
plt.scatter(x_test[:, 1], y_test)
y_test_sorted = y_test.iloc[indices]

model.fit(x_train, y_train)
no_poly_model.fit(x_l_train, y_l_train)

y_predict = model.predict(x_sorted)
y_predict_no_poly = no_poly_model.predict(x_l_test)

plt.plot(x_sorted[:, 1], model.predict(x_sorted), color='red')

plt.figure()
plt.scatter(x_l_test, y_l_test)
plt.plot(x_l_test, y_predict_no_poly, color='red')

print("Polynomial Regression: R2 Score", r2_score(y_test, y_predict))
print("Polynomial Regression: Mean Squared Error", mean_squared_error(y_test, y_predict))

print("Linear Regression: R2 Score", r2_score(y_l_test, y_predict_no_poly))
print("Linear Regression: Mean Squared Error", mean_squared_error(y_l_test, y_predict_no_poly))

x_input_poly = int(input("Entering x value for Polynomial Regression Model:"))
print("Polynomial Regression Prediction:", model.predict(poly_for_x.fit_transform([[x_input_poly]])))
x_input_linear = int(input("Entering x value for Linear Regression Model:"))
print("Linear Regression Prediction:", no_poly_model.predict(np.array(x_input_linear).reshape(1, -1)))

plt.show()

print(y_predict)




