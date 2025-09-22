import pandas as pd
import numpy as np

dictionary_of_series = {
    'TestCase' : pd.Series(['TC1','TC2', 'TC3', 'TC4', 'TC5', 'TC6']),
    'Module'   : pd.Series(['Login', 'Login', 'Payment', 'Payment', 'Reports', 'Reports']),
    'Status'   : pd.Series(['Passed', 'Failed', 'Passed', 'Failed', 'Passed', 'Passed']),
    'Duration' : pd.Series([12, 15, 20, 18, 25, 22]),
}

gp = pd.DataFrame(dictionary_of_series)
print(gp)

group_by_status = gp.groupby("Status").agg(
    count = ('Status', 'count')
    
)
print(gp.groupby("Status")['TestCase'].count())
print(group_by_status)
group_by_module = gp.groupby("Module").agg(
    module = ('Duration', 'mean')
)
print(group_by_module)
print(gp.groupby("Module")['Duration'].mean())

# print(type(gp))



