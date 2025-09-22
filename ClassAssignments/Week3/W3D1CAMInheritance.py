class Employee:

    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

class Tester(Employee):

    private_var = 0

    def __init__(self, name, employee_id):
        super().__init__(name, employee_id)

    def run_tests(self):
        print(self.name, "is running the execution")

cat = Tester("Pradeep", 53)      
cat.run_tests()  
print(cat.name)
print(cat.private_var)
