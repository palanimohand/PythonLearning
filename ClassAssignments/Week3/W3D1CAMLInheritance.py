class Person:

    def __init__(self, name):
        self.name = name

class Employee(Person):

    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id


class Manager(Employee):

    def __init__(self, name, employee_id, team_size):
        super().__init__(name, employee_id)
        self.team_size = team_size

    def show_details(self):
        print(self.name, self.employee_id, self.team_size)

ramesh = Manager("Kumar", "455493", 5)
suresh = Manager("Aravind", "455400", 8)
ramesh.show_details()
suresh.show_details()