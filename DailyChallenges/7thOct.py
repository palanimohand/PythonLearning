import numpy as np

input_array = np.array([10,20,30,40,50])

print(input_array.mean(), np.median(input_array), round(np.std(input_array),2))
print(np.mean(input_array), np.median(input_array), round(np.std(input_array),2))
print(tuple((np.mean(input_array), np.median(input_array), round(np.std(input_array),2))))