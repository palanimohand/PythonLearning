from sklearn.metrics import r2_score,mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("ClassAssignments\Week7\salary.csv")
# print(dataset)

x = dataset[['YearsExperience']] #Feature Doesnt accept single series as an input as there are multiple values in features
y = dataset['Salary'] #Label

print(type(x))
print("_________________")
print(type(y))
print("_________________")
print(x)
print("_________________")
print(y)
print("_________________")

x_train, x_test, y_train, y_test  = train_test_split(x,y, test_size=0.2, random_state=1)

print(x_test,x_train,y_test,y_train)
print(type(x_test))

model = LinearRegression()

model.fit(x_train,y_train)

y_predict = model.predict(x_test)

print(type(y_predict))
print(y_predict)

print(mean_squared_error(y_test,y_predict))
print(r2_score(y_test,y_predict))

plt.scatter(x_test,y_test, label="Data Points")
plt.plot(x_test,y_predict, label="Regression Line", color="red")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.legend()
plt.show()


input_x  = input("Enter Years of Experience : ").split(',')
input_data = pd.DataFrame(pd.Series(input_x),columns=["YearsExperience"])
print(input_data)
input_predict_y = model.predict(input_data)
print(input_predict_y.round())