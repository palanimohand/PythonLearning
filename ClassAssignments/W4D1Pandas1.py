import pandas as pd
import numpy as np

custom_label = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
defects_logged = pd.Series([5, 8, 3, 6, 10, 2, 7], index=custom_label)
defects_logged[custom_label]
print(defects_logged)
print(defects_logged.max())
print(defects_logged.min())
print(defects_logged.idxmin()) #index of min value 
print(defects_logged.iloc[4])
print(defects_logged.loc['Wed'])
print(defects_logged.sum())