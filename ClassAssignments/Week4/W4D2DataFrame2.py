import pandas as pd
import numpy as np
dictionary_of_series = {
    'TestCase' : pd.Series(['TC1','TC2', 'TC3', 'TC4', 'TC5']),
    'Status'   : pd.Series(['Passed', 'Failed', 'Passed', 'Failed', 'Passed']),
    'Duration' : pd.Series([12, 15, 20, 18, 25])
}
ds = pd.DataFrame(dictionary_of_series)
print(ds)
print(ds['Status'])
print(ds[ds['Status']=='Failed'])
ds.to_csv(r"ClassAssignments\Week4\W4D2DataFrame2.csv",index=False)
dd = pd.read_csv(r"ClassAssignments\Week4\W4D2DataFrame2.csv")
print(dd)