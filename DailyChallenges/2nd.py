import numpy as np

# You are given a 2D NumPy array of integers. Your task is to: Compute the sum of each row. Compute the maximum value of each column. Return both as a tuple (row_sums, col_max) where: row_sums is a 1D NumPy array of row-wise sums. col_max is a 1D NumPy array of column-wise maximum values. Example: Input: np.array([ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]) Output: (array([ 6, 15, 24]), array([7, 8, 9]))
sum_array= np.array([], dtype=int)
max_array = np.array([], dtype=int)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9],[10,11,12]])
row, column = arr.shape
# sum_array= np.zeros(row, dtype=int)
# max_array = np.zeros(column, dtype=int)

for a,b in enumerate(arr):
    print(a,b)
    # sum_array[a] = np.sum(arr[a,:])
    sum_array = np.append(sum_array,np.sum(arr[a,:]))
for col in range(column):
    # max_array[col] = np.max(arr[:,col])
    max_array = np.append(max_array,np.max(arr[:,col]))

output = tuple([sum_array,max_array])
print(output)