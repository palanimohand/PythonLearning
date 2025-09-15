# 1. Create a NumPy array with elements 10, 20, 30, 40, 50, 60 using a single-dimensional array. Then, perform the following operations:
# Slice the array using [2:]
# Slice the array using [3:5]
# Access the element using [-4]
# Reverse the array.
# 2. Create a two-dimensional array with a list, and access the following elements:
# Samplearray[0][1]
# Samplearray[1][1]
# Samplearray[0][3]
# Calculate the sum of all elements in the two-dimensional array.
# 3. Create a three-dimensional array named sample3dim, and print the following elements:
# sample3dim[0][0][0]
# sample3dim[0][1][2]
# sample3dim[1][1][2]
# 4. Use ndim to show the dimensions of the arrays created.

import numpy as np

one_d = np.array([10, 20, 30, 40, 50, 60])
print(one_d[2:])
print(one_d[3:5])
print(one_d[-4])
print(one_d[::-1])
print(one_d.ndim)

Samplearray = np.array([[1,3,5,7],[2,4,6,8]])
print(Samplearray[0][1])
print(Samplearray[1][1])
print(Samplearray[0][3])
print(Samplearray.ndim)

sum = 0

for one_d in Samplearray:
    for two_d in one_d:
        sum += two_d

print(sum)

sample3dim = np.array([[[1,3,5],[2,4,6]],[[1,2,3],[4,5,6]]])
print(sample3dim[0][0][0])
print(sample3dim[0][1][2])
print(sample3dim[1][1][2])
print(sample3dim.ndim)

