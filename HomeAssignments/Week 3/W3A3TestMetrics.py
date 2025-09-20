import random
import numpy as np

exe = []
for i in range(50):
    exe.append(random.randint(5,50))
print(exe)

# Using List Comprehension
exe2 = [[random.randint(5, 50) for j in range(50)] for i in range(5)]
print(exe2)
execution_times = np.array(exe2)
print(execution_times)
print(np.max(execution_times))
print(np.mean(execution_times[0,]))
print(np.mean(execution_times[1,]))
print(np.mean(execution_times[2,]))
print(np.mean(execution_times[3,]))
print(np.mean(execution_times[4,]))
print(np.std(execution_times[0,]))
print(np.std(execution_times[1,]))
print(np.std(execution_times[2,]))
print(np.std(execution_times[3,]))
print(np.std(execution_times[4,]))
# slicing operations
print(execution_times[0,:10])
print(execution_times[4,-5:])
print(execution_times[2,::2])
# arthimetic operations
print(np.add(execution_times[0,],execution_times[1,]))
print(np.subtract(execution_times[0,],execution_times[1,]))
print(np.multiply(execution_times[3,],execution_times[4,]))
print(np.divide(execution_times[3,],execution_times[4,]))
# power functions
print(np.sqrt(execution_times))
print(np.square(execution_times))
print(np.power(execution_times,3))
print(np.log(execution_times+1))
# copy operations
execution_times_shallow = execution_times.copy() 
print(execution_times)
print(execution_times_shallow)
execution_times[1,11] = 56
print(execution_times_shallow)
execution_times_deep = execution_times.copy() 
print(execution_times)
print(execution_times_deep)
execution_times[3,5] = 56
print(execution_times_deep)
# filtering and conditions
np.where(execution_times[1,] > 30)
np.where(execution_times > 25)
condition = execution_times < 10
execution_times_filter = execution_times[condition]
print([[10 if i < 10 else int(i) for i in execution_times[j,:]] for j in range(5)])
