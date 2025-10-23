from sklearn.metrics import r2_score,mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("ClassAssignments\Week7\salary.csv")
# print(dataset)

x = dataset[['YearsExperience']] #Feature Doesnt accept single series as an input as there are multiple values in features
y = dataset['Salary'] #Label

# print(x,y)

x_train, x_test, y_train, y_test  = train_test_split(x,y, test_size=0.2, random_state=1)

# print(x_test,x_train,y_test,y_train)
print(type(x_test))

model = LinearRegression()

model.fit(x_train,y_train)

y_predict = model.predict(x_test)

print(y_predict)

print(mean_squared_error(y_test,y_predict))
print(r2_score(y_test,y_predict))

plt.scatter(x_test,y_test)
plt.plot(x_test,y_predict)
plt.show()