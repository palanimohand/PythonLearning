import numpy as np
arr1 = np.array([[1, 2], [3, 4]])  
arr2 = np.array([[5, 6], [7, 8]])
row1, col1 = arr1.shape
print(row1, col1)
row2, col2 = arr2.shape
print(row2, col2)
if row1 != row2:
    print("axis 0 concatenation not possible")
elif col1 != col2:
    print("axis 1 concatenation is not possible")
else:
    output = tuple([np.concat([arr1, arr2], axis=0), np.concat([arr1, arr2], axis=1)])
    print(output)