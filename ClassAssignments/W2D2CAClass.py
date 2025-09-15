class Person:

    def __init__(self, name):
        self.name = name

    def invite(self):
        print("Welcome", self.name)

p1 = Person("Ram")
p2 = Person("Sita")

p1.invite()
p2.invite()