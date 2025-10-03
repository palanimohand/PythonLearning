import pandas as pd

data = pd.read_csv("tt.csv")

print(data)
print(data['Duration'])
print(data['Duration'].describe())
print(data.groupby("Status")['Duration'].mean())
print(data.groupby(["Module","Status"])["Defects"].sum())