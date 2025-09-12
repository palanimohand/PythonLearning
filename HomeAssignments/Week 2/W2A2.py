class Student:
    
    def print_info(self):
        output = "Name : " + self.name + " Grade : " + str(self.grade) + " Department : " + self.dept
        print(output)

    def update_grade(self, new_grade):
        self.grade = new_grade

    def __init__(self, name, grade, dept):
        self.name = name
        self.grade = grade
        self.dept = dept

    def __str__(self):
        output = "Name : " + self.name + " Grade : " + str(self.grade) + " Department : " + self.dept
        return output

if __name__ == "__main__":
    nisha = Student("Nisha", 11, "Computer Science")
    nisha.print_info()
    nisha.update_grade(12)
    nisha.print_info()
    vikram = Student("Vikram", 10, "Commerce")
    print(vikram)