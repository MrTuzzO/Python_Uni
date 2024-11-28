class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def get_details(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year_published}"

book1 =  Book("Django", "Mr. Xyz", 1999)
print(book1.get_details())