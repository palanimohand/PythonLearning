import pandas as pd
import numpy as np

dictionary_of_defects = {
    'DefectID' : ['D1','D2','D3','D4','D5'],
    'Module'   : ['Login','Payment',"Reports",'Login','Payment'],
    'Severity' : ['High','Medium','Low','High','Medium'],
    'Status'   : ['Open','Closed','Open','Closed','Open']
}

new_df = pd.DataFrame(dictionary_of_defects)
print(new_df)
print(new_df["Status"])
print(new_df.groupby("Status")['Status'].count())
print(new_df["Status"]=="Open")

print(new_df[new_df["Status"]=="Open"]["DefectID"])
print(new_df[new_df["Status"]=="Open"]["DefectID"].count())
print(new_df.groupby('Severity')['DefectID'].count())
print(new_df[new_df['Severity']=="High"])
print(new_df.groupby("Status")['Status'].count())
print(type(new_df.groupby("Status")['Status'].count()))