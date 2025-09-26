import kagglehub
import shutil
import os
import numpy as np
import pandas as pd

"""
path = kagglehub.dataset_download("imdevskp/corona-virus-report")

print("Path to dataset files:", path)

source_dir = path
dest_dir = r"C:\Users\Palanimohan\Desktop\AI Engineer\Python_Practice\HomeAssignments\Week 4\Dataset"

for filename in os.listdir(source_dir):
    src_file = os.path.join(source_dir, filename)
    dst_file = os.path.join(dest_dir, filename)
    if os.path.isfile(src_file):
        shutil.copy(src_file, dst_file)
"""

# 1. Summarize Case Counts by Region
# o Display total confirmed, death, and recovered cases for each region.
df = pd.read_csv(r'HomeAssignments\Week 4\Dataset\country_wise_latest.csv',header=0,index_col=0)
print(df)
print(pd.concat([df['Confirmed'],df['Deaths'],df['Recovered']],axis=1))
# 2. Filter Low Case Records
# o Exclude entries where confirmed cases are < 10.
print(df[df['Confirmed']<10])
# 3. Identify Region with Highest Confirmed Cases
print(df['Confirmed'].idxmax(),df['Confirmed'].max())
# 4. Sort Data by Confirmed Cases
# o Save sorted dataset into a new CSV file.
print(df['Confirmed'].sort_values().to_csv("Test.CSV",index=True))
# 5. Top 5 Countries by Case Count
print(df['Confirmed'].sort_values(ascending=False).head())
# 6. Region with Lowest Death Count
print(df['Deaths'].sort_values().idxmin(), df['Deaths'].sort_values().min())
# 7. India’s Case Summary (as of April 29, 2020)
print(df.loc['India',:])
# 8. Calculate Mortality Rate by Region
# o Death-to-confirmed case ratio.
print(df['Deaths']/df['Confirmed']*100)
# 9. Compare Recovery Rates Across Regions
print(df['Recovered']/df['Confirmed']*100)
# 12. Identify Regions with Zero Recovered Cases
print(df[df['Recovered']==0]['Recovered'])
# 11. Group Data by Country and Region
ds = pd.DataFrame(df.groupby("WHO Region",group_keys=True))
print(ds)
for index in range(len(set(df['WHO Region'].unique()))):
    print(ds[1][index])
# 10. Detect Outliers in Case Counts
#  Use mean ± 2*std deviation.
lower = df['Deaths'].mean() - (df['Deaths'].std()*2)
upper = df['Deaths'].mean() + (df['Deaths'].std()*2)
print(lower,upper)
print(df[(df['Deaths']<upper) & (df['Deaths']>lower)]['Deaths'])
lower = df['Confirmed'].mean() - (df['Confirmed'].std()*2)
upper = df['Confirmed'].mean() + (df['Confirmed'].std()*2)
print(lower,upper)
print(df[(df['Confirmed']<upper) & (df['Confirmed']>lower)]['Confirmed'])
lower = df['Recovered'].mean() - (df['Recovered'].std()*2)
upper = df['Recovered'].mean() + (df['Recovered'].std()*2)
print(lower,upper)
print(df[(df['Recovered']<upper) & (df['Recovered']>lower)]['Recovered'])
lower = df['Active'].mean() - (df['Active'].std()*2)
upper = df['Active'].mean() + (df['Active'].std()*2)
print(lower,upper)
print(df[(df['Active']<upper) & (df['Active']>lower)]['Active'])
lower = df['New cases'].mean() - (df['New cases'].std()*2)
upper = df['New cases'].mean() + (df['New cases'].std()*2)
print(lower,upper)
print(df[(df['New cases']<upper) & (df['New cases']>lower)]['New cases'])

