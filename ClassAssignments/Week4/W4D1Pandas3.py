import pandas as pd
import numpy as np

test_pass_rate = pd.Series([80, 85, 78, 90, 88], index=['B1','B2','B3','B4','B5'])
print(test_pass_rate)
print(test_pass_rate.mean())
print(test_pass_rate.idxmax())
print(test_pass_rate.iloc[-1])
print(test_pass_rate.loc['B3'])
print(test_pass_rate - test_pass_rate.mean())