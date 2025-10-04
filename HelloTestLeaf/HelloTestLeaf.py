print("Welcome to Test Leaf")


def ret():
    return 1, 2

_, d = ret()
print(_, d)

import pandas as pd

data = {'Name':['Alice', 'Bob', 'Charlie'], 'Age':[25,30,35]}
df = pd.DataFrame(data)
print(df)