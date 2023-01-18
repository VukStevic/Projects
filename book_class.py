

class Book:
    def __init__(self, title: str, author: str, year: int, genre: str, number_of_pages: int):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.number_of_pages = number_of_pages
        self.number_of_copies = 3

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nYear of publication: {self.year}.\n" \
               f"Genre: {self.genre}\nNumber of pages: {self.number_of_pages}"

    def set_number_of_copies(self, number_of_copies: int):
        """Sets the number of copies available"""
        self.number_of_copies = number_of_copies

    def is_available(self):
        """Returns a boolean representing book's availability"""
        if self.number_of_copies > 0:
            return True
        else:
            return False
