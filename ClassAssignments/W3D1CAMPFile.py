with open("report.txt", "w") as f:
    f.write("TestCase1 - Passed\n")
    f.write("TestCase2 - Failed\n")
    f.write("TestCase3 - Passed\n")

with open("report.txt", "a") as f:
    f.write("TestCase4 - Passed\n")
    f.write("TestCase5 - Failed\n")

with open("report.txt", "r") as f:
    content = f.read()
    print(f.name)
    print(f.mode)
    print(f.closed)

list_of_content = content.split("\n")
print(list_of_content)
print("Total Test cases -", len(list_of_content))
passed_count = content.count("Passed")
failed_count = content.count("Failed")
print("Passed Cases -", passed_count)
print("Failed Cases -", failed_count)