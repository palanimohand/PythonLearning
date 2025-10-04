import matplotlib.pyplot as plt
import pandas as pd

data = {
"Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
"Week1": [1000, 2000, 3000, 5000, 7000, 8000, 6700],
"Week2": [4000, 5000, 2500, 4500, 3500, 5000, 5600],
"Week3": [5000, 6000, 4500, 3500, 2000, 6000, 4800],
"Week4": [6000, 5000, 2900, 4500, 3500, 4500, 4500]
}

panda_data = pd.DataFrame(data)
panda_data.plot(kind="line").figure.savefig(r"ClassAssignments\Week5\Plot_Images\1.JPG")
panda_data.plot(kind="bar").figure.savefig(r"ClassAssignments\Week5\Plot_Images\2.JPG")
panda_data.plot(kind="hist").figure.savefig(r"ClassAssignments\Week5\Plot_Images\3.JPG")
