import pandas as pd
"""
You are given student marks in
different subjects in the form of a
dictionary with keys "Name", "Math",
"Science", and "English". Your task is to:
1. Convert this dictionary into a Pandas
DataFrame. 2. Calculate the average
marks for each subject. 3. Return the
averages in a dictionary with subject
names as keys. Example: · Input: · { ·
"Name": ["Alice", "Bob", "Charlie"], .
"Math": [80, 70, 90], · "Science": [85, 75,
95], · "English": [78, 82, 88] · } · Output:
{"Math": 80.0, "Science": 85.0, "English":
82.67} (round averages to 2 decimal places)
"""

dict={
    "Name" : ["Alice", "Bob", "Charlie"],
    "Math" : [80, 70, 90],
    "Science" : [85, 75, 95],
    "English" : [78, 82, 88],
}

data = pd.DataFrame(dict)
print(data) 
print(data.columns[0]) #prints the column name at that index
data = data.set_index('Name') #sets the column name and its values as row index
print(data)
print(data['Math'].mean(),data['Science'].mean(),data['English'].mean())
row, column = data.shape
output_dict = {}
for i in range(column):
    output_dict.update({data.columns[i]:round(float(data[data.columns[i]].mean()),2)})
print(output_dict)