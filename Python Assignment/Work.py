from abc import ABC, abstractmethod


class Book(ABC):# first class
    def __init__(self, title, author, isbn):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._available = True  

#use of abstraction
    @abstractmethod 
    def checkout(self):
        pass

    def is_available(self):
        return self._available

    # encapsulation is applied 
    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def isbn(self):
        return self._isbn

# BorrowableBook inherits from Book 

class BorrowableBook(Book): #second class
    def checkout(self):
        if self._available:
            self._available = False
            print(f"'{self.title}' checked out.")
        else:
            print(f"'{self.title}' is not available.")

    def return_book(self):
        if not self._available:
            self._available = True
            print(f"'{self.title}' returned.")
        else:
            print(f"'{self.title}' is already available.")


class Library:# third class
    def __init__(self):
        self._catalog = {}

    def add_book(self, book):
        self._catalog[book.isbn] = book
        print(f"Added '{book.title}' to the catalog.")

    def remove_book(self, isbn):
        if self._catalog.pop(isbn, None):
            print("Book removed from catalog.")
        else:
            print("Book not found.")

    def checkout_book(self, isbn):
        book = self._catalog.get(isbn)
        if book:
            book.checkout()
        else:
            print("Book not found.")

    def return_book(self, isbn):
        book = self._catalog.get(isbn)
        if book and isinstance(book, BorrowableBook):
            book.return_book()
        else:
            print("Book not found or not borrowable.")

    def display_catalog(self):
        if not self._catalog:
            print("Library catalog is empty.")
        else:
            for book in self._catalog.values():
                status = "Available" if book.is_available() else "Checked Out"
                print(f"{book.title} by {book.author} (ISBN: {book.isbn}) - {status}")

# Interactive menu for library system
def library_system():
    library = Library()
    options = {
        '1': ("Add Book", lambda: library.add_book(
            BorrowableBook(input("Title: "), input("Author: "), input("ISBN: ")))),
        '2': ("Remove Book", lambda: library.remove_book(input("ISBN to remove: "))),
        '3': ("Checkout Book", lambda: library.checkout_book(input("ISBN to checkout: "))),
        '4': ("Return Book", lambda: library.return_book(input("ISBN to return: "))),
        '5': ("Display Catalog", library.display_catalog)
    }

    while True:
        print("\nLibrary Menu:")
        for key, (desc, _) in options.items():
            print(f"{key}. {desc}")
        print("6. Exit")

        choice = input("Choose an option: ")
        if choice == '6':
            print("Exiting Library System. Goodbye!")
            break
        options.get(choice, (None, lambda: print("Invalid option")))[1]()

# Run the interactive library system
library_system()
