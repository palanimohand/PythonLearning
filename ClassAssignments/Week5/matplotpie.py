import matplotlib.pyplot as plt

High = 10
Medium = 15
Low = 5

plt.pie([High, Medium, Low],labels=["High", "Medium", "Low"],autopct='%1.1f%%',startangle=90)
plt.title("Defect Distribution by Severity")
plt.show()