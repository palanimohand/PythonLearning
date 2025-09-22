import numpy as np

one_array = np.array([10, 15, 20, 25, 30, 35, 40, 45])
print(one_array[0])
print(one_array[-1])
print(one_array[2])
print(one_array.shape)
print(one_array[0:3])
print(one_array[::2])
print(one_array.reshape(2,4))
two_array = np.array([50, 55, 60, 65])
print(np.concatenate([one_array, two_array]))
print(np.array_split(one_array,2))