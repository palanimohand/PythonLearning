import matplotlib.pyplot as plt

Passed = 45
Failed = 10
Skipped = 5  

plt.bar(["Passed", "Failed", "Skipped"],[Passed, Failed, Skipped],color=["green","red","blue"],edgecolor="black")
plt.xlabel("Test Status")
plt.ylabel("Number of Test Cases")
plt.title("Test Execution Results")
# plt.xticks([5,10])
plt.savefig('Test.png')



plt.show()