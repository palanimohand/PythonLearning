import pandas as pd
import numpy as np

test_execution_times = pd.Series([12, 15, 20, 18, 25, 30, 22], index=['TC1','TC2','TC3','TC4','TC5','TC6','TC7'])
print(test_execution_times.head(3))
print(test_execution_times.mean())
print(test_execution_times.iloc[1])
print(test_execution_times.loc['TC3'])