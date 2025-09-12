import datetime


class Book:

    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def get_age(self):
        current_year = datetime.datetime.now().year
        age = current_year - self.publication_year
        return age

ponniyin_selvan = Book("Ponniyin_Selvan", "Kalki", 1955)
print("Age of Book is :", ponniyin_selvan.get_age())