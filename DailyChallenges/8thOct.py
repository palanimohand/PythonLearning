import numpy as np
row = 5
col = 1
arr = np.array([1,2,3,4,5,6])
if row*col == arr.size:
    print(arr.reshape(row,col))
else:
    print("Reshape not possible for this dimensions")