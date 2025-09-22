import pandas as pd
import numpy as np

array_1 = np.array([10,20,30])
array_2 = np.array([30,40,50])
numpy_df = pd.DataFrame([array_1, array_2])
print(numpy_df)

series_1 = pd.Series([100,200,300])
series_2 = pd.Series([400,500])
series_df = pd.DataFrame([series_1, series_2])
print(series_df)

dictionary_of_series = {
    'Mani' : pd.Series([10,20,30]),
    "Alex" : pd.Series([20,30])
}
dictionary_of_series_df = pd.DataFrame(dictionary_of_series)
print(dictionary_of_series_df)