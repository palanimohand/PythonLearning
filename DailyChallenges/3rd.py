import numpy as np

arr = np.array([4,2,7,2,4,9])
unique_array = np.array(list(set(arr)))
unique_array.sort()
print(unique_array)