from library_class import Library
from datetime import datetime


class Customer:
    def __init__(self, name: str, surname: str, id_num: str, cellphone_number: str, landline_number: str):
        self.name = name
        self.surname = surname
        self.__id = id_num
        self.cellphone_number = cellphone_number
        self.landline_number = landline_number
        self.borrowed_books = []

    def get_id(self):
        """Returns customer's ID number"""
        return self.__id

    def __str__(self):
        return f"Name: {self.name}\nSurname: {self.surname}\nID number: {self.get_id()}\n" \
               f"Cellphone number: {self.cellphone_number}\nLandline number: {self.landline_number}"

    def borrow(self, library: Library, book_title: str):
        """Borrows a book from the library, if the book is available"""
        found = 0
        for book in library.books:
            if book.title.lower() == book_title.lower():
                found += 1
                if book.is_available():
                    self.borrowed_books.append([book, datetime.today().strftime("%d-%b-%Y")])
                    library.lent_books.append([book, self])
                    book.number_of_copies -= 1
                else:
                    print("Book is currently unavailable.")
        if found == 0:
            print("Book not found.")

    def return_book(self, library, book_title: str):
        """Removes the book from the list of borrowed books and adds it to the library's list of available books"""
        found = 0
        for book in self.borrowed_books:
            borrowed_book = book[0]
            if borrowed_book.title.lower() == book_title.lower():
                found += 1
                self.borrowed_books.remove(book)
                library.lent_books.remove([borrowed_book, self])
                borrowed_book.number_of_copies += 1
        if found == 0:
            print("Book is either not borrowed or already returned.")

    def get_borrow_date(self, book_title: str):
        """Returns the date a book was borrowed if the book title is found in the list of borrowed books"""
        for book in self.borrowed_books:
            borrowed_book = book[0]
            date = book[1]
            if borrowed_book.title.lower() == book_title.lower():
                return date

    def is_within_deadline(self, book_title: str):
        """Checks if the book is borrowed by the user and if it is, it checks if deadline is exceeded or not"""
        from library_class import Library
        found = 0
        for book in self.borrowed_books:
            borrowed_book = book[0]
            if borrowed_book.title.lower() == book_title.lower():
                found += 1
                date = self.get_borrow_date(book_title)
                days_gone = datetime.today() - datetime.strptime(date, "%d-%b-%Y")
                return Library.DEADLINE >= days_gone.days
        if found == 0:
            return 0

    def show_borrowed_books(self):
        """Prints all the books currently borrowed by the customer along with borrowing dates"""
        for book in self.borrowed_books:
            print(f"{book[0]}\nBorrowing date: {book[1]}")
            print("----------")
