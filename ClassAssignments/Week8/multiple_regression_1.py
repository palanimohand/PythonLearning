from sklearn.metrics import r2_score,mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import axes3d
import numpy as np

input_data = pd.DataFrame({
    "x1" : [1,2,3],
    "x2" : [2,1,4]
})

print(input_data)

y = pd.Series([6,8,14])

print(y)

x_train = input_data
x_test = input_data
y_train = y
y_test = y

model = LinearRegression()

model.fit(x_train,y_train)

y_predict = model.predict(x_test)

print(type(y_predict),y_predict)

print(model.coef_)
print(model.intercept_)

print(r2_score(y_test,y_predict))
print(mean_squared_error(y_test,y_predict))

# plt.figure()
# plt.scatter(x_test, y_test)
# plt.plot(x_test,y_predict)
# plt.show()

X = np.asarray(x_test['x1'])
Y = np.asarray(x_test['x2'])
Z = np.asarray(y_test)           # currently shape (3,1)

print("shapes:", X.shape, Y.shape, Z.shape)
Xb, Yb, Zb = np.broadcast_arrays(X, Y, Z)
print("broadcast shape:", Xb.shape)
print(Xb,Yb,Zb) 
points = list(zip(Xb.ravel(), Yb.ravel(), Zb.ravel()))
print("points plotted (after broadcast):")
print(points)

fig = plt.figure(figsize=(30, 21))
ax = fig.add_subplot(111, projection="3d")
print((x_test['x1'].tolist(), x_test['x2'].tolist(), y_test))
ax.scatter(x_test['x1'],x_test['x2'],y_test, color="blue", label="Actual Data", s=100)
# annotate actual data points with their (x1,x2,y) values
for xi, xj, zk in zip(x_test['x1'].values, x_test['x2'].values, y_test.values):
    ax.text(xi, xj, zk, f"({xi},{xj},{zk})", size=8, zorder=5, color='blue')

x1_plane = np.linspace(input_data['x1'].min(), input_data['x1'].max(), 10) 
x2_plane = np.linspace(input_data['x2'].min(), input_data['x2'].max(), 10)

x1_plane, x2_plane = np.meshgrid(x1_plane,x2_plane)

print(x1_plane)
print("++++++++++++++++++++")
print(x1_plane.ravel())

# y_predict = y_predict.reshape(xone.shape)

y_predict = model.predict(pd.DataFrame({'x1':x1_plane.ravel(),'x2':x2_plane.ravel()}))

print(y_predict)

y_predict = y_predict.reshape(x1_plane.shape)

print(y_predict)

# build a DataFrame of the grid + predicted z
grid_df = pd.DataFrame({
    'x1': x1_plane.ravel(),
    'x2': x2_plane.ravel()
})
z_pred = model.predict(grid_df)                     # shape (100,)
surface_points = pd.DataFrame({
    'x1': grid_df['x1'],
    'x2': grid_df['x2'],
    'y_pred': z_pred
})

# show summary and first rows
print(f"Total surface points: {len(surface_points)}")   # 100 for 10x10 grid
print(surface_points.head(10))                          # first 10 points
# optional: show every point
# print(surface_points.to_string(index=False))

# optional: save to CSV for inspection
surface_points.to_csv('surface_points.csv', index=False)
print('Saved surface points -> surface_points.csv')

# Plot the regression plane
print(list(zip(x1_plane.tolist(),x2_plane.tolist(),y_predict.tolist())))
# scatter the predicted grid points for visual verification
ax.scatter(surface_points['x1'], surface_points['x2'], surface_points['y_pred'],
           color='green', s=12, alpha=0.45, label='Predicted points')
ax.plot_surface(x1_plane, x2_plane, y_predict, color='red', alpha=0.3, label='Predicted Plane')
# annotate all predicted grid points with their predicted values
for idx, r in surface_points.iterrows():
    # show full (x1, x2, y_pred) triple for each predicted point
    ax.text(
        r['x1'],
        r['x2'],
        r['y_pred'],
        f"({r['x1']:.2f}, {r['x2']:.2f}, {r['y_pred']:.2f})",
        size=6,
        color='green',
        alpha=0.7,
    )
ax.set_xlabel("X1")
ax.set_ylabel("X2")
ax.set_zlabel("Y")
ax.legend()
fig.savefig("3d.png")
plt.show()

