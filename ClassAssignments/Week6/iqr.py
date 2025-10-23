import pandas as pd

sales_data = pd.read_csv(r"ClassAssignments\Week6\SalesDataset_1.csv")

q1 = sales_data['Total Amount'].quantile(0.25)
q3 = sales_data['Total Amount'].quantile(0.75)
print(q1,q3)

iqr = q3 - q1
print(iqr)

lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)
print(lower_bound, upper_bound)

outliers = sales_data[(sales_data['Total Amount'] < lower_bound) | (sales_data['Total Amount'] > upper_bound)]
print(outliers)
print(outliers.shape)

outliers.to_csv("ClassAssignments\Week6\Outliers.csv")

cleaned_data = sales_data[(sales_data['Total Amount'] >= lower_bound) & (sales_data['Total Amount'] <= upper_bound)]
print(cleaned_data)

cleaned_data.to_csv('ClassAssignments\Week6\CleanedData.csv')