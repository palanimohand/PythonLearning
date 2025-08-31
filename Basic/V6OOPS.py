import random

def serialNumberGenerator():
    print("serialNum: ",random.randint(10000,99999))

class Library:
    pass

class Book:
    # bookname
    # author

    # any name as kwargs
    def __init__(self, name, **booklist):
        self.book_list = booklist
        self.name = name

    def __str__(self):
        return self.name

    def borrow(self, book_name):
        if book_name in self.book_list:
            print("Book Borrowed - ",book_name)

    def surrender(self, book_name):
        if book_name not in self.book_list:
            print("Book Surrendered - ", book_name)
            print(id(self))

class Journal(Book):
    def journalMethod(self):
        print("Journal Method from Journal")

class Librarian:
    def journalMethod(self):
        print("Journal Method from Librarian")

class Paper(Librarian,Journal):
    def paperMethod(self, a):
        print("Paper Method")

    def paperMethod(self,a,b):
        print("Polymorphism paper method")



class People:
    #     Borrower
    #     Returner
    pass

booklist = ["asura", "chegizkhan", "5am club", "5 love language"]

asura = Book("asura", asura=50, chengizkhan=10)
print(id(asura))
print(type(asura))
asura.borrow("asura")

# print anything multiple number of times
print("-"*25)

resurrection = Book("resurrection", lovelanguage=10, am_club=50)
print(id(resurrection))
print(type(resurrection))
resurrection.surrender("resurrection")
print(resurrection)

pap = Paper("Padipagam", tamil=15, english=20)
pap.borrow("tamil")
print(Paper.__mro__)

pap.journalMethod()
pap.paperMethod(1)
pap.paperMethod(1,2)

# try calling directly like co pilot suggested Journal.commonMethod(self)

