import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from sklearn.metrics import r2_score, mean_squared_error

class StudentPerformanceModel:

    student_performance_data = pd.read_csv(r"HomeAssignments\Week 8\Student_Performance.csv")
    student_performance_data = student_performance_data.drop(columns='Extracurricular Activities')
    # x['Extracurricular Activities'] = [1 if x=="Yes" else 0 for x in x['Extracurricular Activities']] # code to Convert Yes or No to 1 or 0
    
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')

    # Built - in EDA
    print(student_performance_data)
    print(student_performance_data.describe())
    print(student_performance_data.corr())
    print(student_performance_data.var())
    print(student_performance_data.isna().sum()) 
    mean = student_performance_data['Sample Question Papers Practiced'].mean()
    std = student_performance_data['Sample Question Papers Practiced'].std()
    z_score=[]
    for x in student_performance_data['Sample Question Papers Practiced']:
        z_score.append((x-mean)/std)
    print(z_score)
    outliers = student_performance_data['Sample Question Papers Practiced'][np.abs(z_score) > 3]
    print(outliers)
        

    x = student_performance_data[['Hours Studied', 'Previous Scores', 'Sleep Hours', 'Sample Question Papers Practiced']]
    x_with_two = student_performance_data[['Hours Studied', 'Previous Scores']]

    y = student_performance_data['Performance Index']

    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=30)
    x2_train, x2_test, y2_train, y2_test = train_test_split(x_with_two, y, test_size=0.2, random_state=20)

    model = LinearRegression()
    model2 = LinearRegression()

    model.fit(x_train, y_train)
    model2.fit(x2_train, y2_train)

    y_predict = model.predict(x_test)
    y2_predict = model2.predict(x2_test)

    ax.scatter(x_test['Hours Studied'],x_test['Previous Scores'], y_test, color="red")
    ax = plt.figure().add_subplot(111,projection='3d')
    ax.scatter(x2_test['Hours Studied'],x2_test['Previous Scores'], y2_test, color="blue")

    print(model.intercept_)
    print(model.coef_)
    print(model.intercept_)
    print(model.coef_)

    print(r2_score(y_test, y_predict))
    print(r2_score(y2_test, y2_predict))
    print(mean_squared_error(y_test, y_predict))
    print(mean_squared_error(y2_test, y2_predict))

    print(f"formula : y = {model.intercept_:.2f} + {model.coef_[0]:.2f}x1 + {model.coef_[1]:.2f}x2 + {model.coef_[2]:.2f}x3 + {model.coef_[3]:.2f}x4")

    x1 = np.linspace(x_test['Hours Studied'].min(),x_test['Hours Studied'].max(),10)
    x2 = np.linspace(x_test['Previous Scores'].min(),x_test['Previous Scores'].max(),10)
    x3 = np.linspace(x_test['Sleep Hours'].min(),x_test['Sleep Hours'].max(),10)
    x4 = np.linspace(x_test['Sample Question Papers Practiced'].min(),x_test['Sample Question Papers Practiced'].max(),10)

    x1,x2 = np.meshgrid(x1,x2)
    x3,x4 = np.meshgrid(x3,x4)

    x_test = pd.DataFrame({
        'Hours Studied' : x1.ravel(),
        'Previous Scores' : x2.ravel(),
        # 'Sleep Hours' : x3.ravel(),
        # 'Sample Question Papers Practiced' : x4.ravel(),
    })

    # y_predict = model.predict(x_test)


    # y_predict = y_predict.reshape(x1.shape)
    # print(x1.shape, y_predict.shape)

  

    # ax.plot_surface(x1,x2,y_predict,color='red', alpha=0.3, label='Predicted Plane')
    
    plt.show()