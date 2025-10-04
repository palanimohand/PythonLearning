import matplotlib.pyplot as plt

Passed = 45
Failed = 10
Skipped = 5  

plt.bar(["Passed", "Failed", "Skipped"],[Passed, Failed, Skipped],color=["green","red","blue"],edgecolor="black")
plt.xlabel("Test Status")
plt.ylabel("Number of Test Cases")
plt.title("Test Execution Results")
# plt.xticks([5,10])
plt.savefig(r'ClassAssignments\Week5\matplotlib1.png')



plt.show()