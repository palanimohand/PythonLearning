from sklearn.preprocessing import RobustScaler,MinMaxScaler,StandardScaler
import numpy as np

data = np.array([[1,2],[3,4],[5,6],[7,8],[9,10]])

print(data)

technique_1 = MinMaxScaler()
technique_2 = RobustScaler()
technique_3 = StandardScaler()

print(technique_1.fit_transform(data))
print(technique_2.fit_transform(data))
print(technique_3.fit_transform(data))