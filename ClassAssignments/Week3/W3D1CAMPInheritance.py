class Employee:

    def __init__(self, name):
        self.name = name

class Automation_Skills:

    def write_script(self):
        print("Writing Selenium Scripts")

class Automation_Tester(Employee, Automation_Skills):

    def execute_tests(self):
        print("Executing Automation Suite")

master = Automation_Tester("Suresh")
master.execute_tests()
master.write_script()
