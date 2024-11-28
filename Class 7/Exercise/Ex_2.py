class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f"Book title: {self.title}")
        print(f"Author: {self.author}")

book1 = Book("Python", "John Deo")
book1.display()