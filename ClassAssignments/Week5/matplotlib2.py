import matplotlib.pyplot as plt

Weeks = [1, 2, 3, 4, 5, 6]
Defects = [5, 8, 6, 10, 7, 4]

plt.plot(Weeks,Defects,marker='D')
plt.xlabel("Week Number")
plt.ylabel("Number of Defects")
plt.title("Defect Trend Over Time")
plt.grid(True)
plt.show()