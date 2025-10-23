from sklearn.preprocessing import StandardScaler
# import sklearn.preprocessing as jk
import numpy as np

# jk.StandardScaler()

data = np.array([[1, 2],[3,4],[5,6]])
sc = StandardScaler()     
print(data)                 
print(sc.fit_transform(data))