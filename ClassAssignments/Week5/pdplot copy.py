import matplotlib.pyplot as plt
import pandas as pd

data_2 = {'Module':['AI', 'ML', 'Python', 'DataStructures'], 'Teamsize':[135, 125, 125, 115] }
xa = data_2['Module']
print(xa)
ya = data_2['Teamsize']
print(ya)
panda_data2 = pd.DataFrame(data_2)

panda_data2.plot(kind="pie",y="Teamsize",startangle=90, legend=True).figure.savefig("4.JPG")