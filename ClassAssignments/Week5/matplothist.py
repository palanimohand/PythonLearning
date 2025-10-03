import matplotlib.pyplot as plt

execution_times = [12, 15, 20, 18, 22, 30, 25, 16, 19, 28, 24, 14]
plt.hist(execution_times,bins=5,color="green",edgecolor="yellow")
plt.xlabel("Duration (seconds)")
plt.ylabel("Number of Test Cases")
plt.title("Distribution of Test Execution Times")
plt.show()