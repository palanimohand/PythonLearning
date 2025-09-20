class Employee:

    name=None
    emp_id=None
    department=None

    def __init__(self, name, emp_id, department):
        self.name = name
        self.emp_id = emp_id
        self.department = department

    def display_info(self):
        print(self.name, self.emp_id, self.department)

class Manager(Employee):

    team_size=0

    def __init__(self, name, emp_id, department, team_size):
        super().__init__(name, emp_id, department)
        self.team_size = team_size

    def display_info(self):
        print(self.name, self.emp_id, self.department, self.team_size)
    
class Developer(Employee):

    programming_language=""

    def __init__(self, name, emp_id, department, programming_language):
        super().__init__(name, emp_id, department)
        self.programming_language = programming_language

    def display_info(self):
        print(self.name, self.emp_id, self.department, self.programming_language)
    
if __name__ == "__main__":

    my_manager = Manager("Tim Cook", "IAE1452", "CEO", 10000)
    my_manager.display_info()
    iam_developer = Developer("Palanimohan", "IAE5500", "Architect", "Java,Python,Groovy")
    iam_developer.display_info()
