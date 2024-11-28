class Library:
    def __init__(self):
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        print(f"'{book}' has been added.")

    def removeBook(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"'{book}' has been removed.")
        else:
            print(f"Book {book.title} does not exist.")

    def displayBooks(self):
        print("Books in Library: ", self.books)


library = Library()
library.addBook("The great GatSby")
library.addBook("Python")
library.addBook("C++")
library.addBook("Algorithms")

library.displayBooks()
library.removeBook("The great GatSby")
library.displayBooks()
