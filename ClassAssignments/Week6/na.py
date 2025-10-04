import pandas as pd

data = [["TestCase","Module","Status","Duration","Defects"],["TC1","Login","Passed",12,0],["TC2","Login","Failed",None,2],["TC3","Payment","Passed",20,None],["TC4","Payment","Failed",18,3],["TC5","Reports",None,25,0]]
na_data = pd.DataFrame(data)
na_data.to_csv(r"ClassAssignments\Week6\naDataSet.csv",index=False,header=False)
na_data_from_csv = pd.read_csv(r"ClassAssignments\Week6\naDataSet.csv",index_col=0)
print(na_data)
print(na_data.isnull().sum())
print(sum(na_data.isnull().sum()))
print(na_data_from_csv)
na_data_from_csv["Status"] = na_data_from_csv["Status"].fillna("Unknown")
na_data_from_csv["Duration"] = na_data_from_csv["Duration"].fillna(na_data_from_csv["Duration"].mean())
print(na_data_from_csv)
na_data_from_csv.dropna(inplace=True)
print(na_data_from_csv)