from datetime import datetime
from book_class import Book


class Library:

    DEADLINE = 30

    def __init__(self):
        self.books = []
        self.lent_books = []
        self.customers = []
        self.employees = []
        self.__membership_fee = 10
        self.__utility_costs = 500

    def read_books_from_file(self, file):
        """Reads the text file containing books and their info, makes a Book object
           for each of them and puts it in the library's list of books"""
        with open(file, "r") as f:
            lines = f.readlines()
        for line in lines[1:]:
            book = line.split("    ")
            title = book[0].strip()
            author = book[1].strip()
            year = int(book[2].strip())
            genre = book[3].strip()
            number_of_pages = int(book[4].strip())
            self.books.append(Book(title, author, year, genre, number_of_pages))

    def read_employees_from_file(self, file):
        """Reads the text file containing employees and their info, and
           puts them in the library's list of employees"""
        from employee_class import Employee
        with open(file, "r") as f:
            lines = f.readlines()
        for line in lines[1:]:
            employee = line.split("    ")
            name = employee[0].strip()
            surname = employee[1].strip()
            id_num = employee[2].strip()
            cellphone_number = employee[3].strip()
            landline_number = employee[4].strip()
            position = employee[5].strip()
            salary = int(employee[6].strip())
            self.employees.append(Employee(name, surname, id_num, cellphone_number, landline_number, position, salary))

    def add_books(self, book: Book):
        """Adds a book to the library's list of books"""
        self.books.append(book)

    def remove_books(self, book_title: str):
        """Removes a book from the library's list of books"""
        found = 0
        for book in self.books:
            if book.title.lower() == book_title.lower():
                found += 1
                self.books.remove(book)
        if found == 0:
            return 0

    def is_available(self, book_title: str) -> bool:
        """Takes a book title in the form of a string and returns a boolean representing book's availability"""
        for book in self.books:
            if book_title.lower() == book.title.lower():
                if book.number_of_copies > 0:
                    return True
                return False

    def show_all_books(self):
        """Prints the titles of all the books owned by the library"""
        for i, book in enumerate(self.books):
            print(f"{i + 1}) {book.title}")

    def show_available_books(self):
        """Prints the titles of all the available books along with the number of currently available copies"""
        available_books = []
        for book in self.books:
            if book.is_available():
                available_books.append(book)
        for i, book in enumerate(available_books):
            print(f"{i + 1}) {book.title} >> Available copies: {book.number_of_copies}")

    def show_lent_books(self):
        """Prints the info of all the books currently lent out to customers along with the borrowing date
         and whether the deadline is exceeded or not"""
        for book in self.lent_books:
            lent_book = book[0]
            customer = book[1]
            date = customer.get_borrow_date(lent_book.title)
            days_gone = datetime.today() - datetime.strptime(date, "%d-%b-%Y")
            days_gone = days_gone.days
            if days_gone > Library.DEADLINE:
                print(f"Book title: {lent_book.title}\n{customer.name} {customer.surname},"
                      f" ID: {customer.get_id()}\nBorrow date: {date}\nDays gone: {days_gone} >> Deadline exceeded.")
                print("---------")
            else:
                print(f"Book title: {lent_book.title}\n{customer.name} {customer.surname},"
                      f" ID: {customer.get_id()}\nBorrow date: {date}\nDays gone: {days_gone}")
                print("---------")

    def books_by_title(self, title: str):
        """Prints books written by a given title"""
        books_found = 0
        for book in self.books:
            if book.title.lower() == title.lower():
                books_found += 1
                print(book)
                print("------")
        if books_found == 0:
            return 0

    def book_by_title(self, title: str):
        """Prints books written by a given title"""
        books_found = 0
        for book in self.books:
            if book.title.lower() == title.lower():
                books_found += 1
                return book
        if books_found == 0:
            return 0

    def books_by_author(self, author: str):
        """Prints books written by a given author"""
        books_found = 0
        for book in self.books:
            if book.author.lower() == author.lower():
                books_found += 1
                print(book)
                print("------")
        if books_found == 0:
            print("No books found by a given author.")

    def books_by_genre(self, genre: str):
        """Prints books by a given genre"""
        books_found = 0
        for book in self.books:
            if book.genre.lower() == genre.lower():
                books_found += 1
                print(book)
                print("------")
        if books_found == 0:
            print("No books found by a given genre.")

    def books_by_year(self, year: int):
        """Prints books written in given year"""
        books_found = 0
        for book in self.books:
            if book.year == year:
                books_found += 1
                print(book)
                print("------")
        if books_found == 0:
            print("No books found by a given year.")

    def books_by_period(self, starting_year: int, ending_year: int):
        """Prints books written in a given year period"""
        books_found = 0
        for book in self.books:
            if starting_year <= book.year <= ending_year:
                books_found += 1
                print(book)
                print("------")
        if books_found == 0:
            print("No books found in a given period.")

    def books_by_number_of_pages(self, min_pages: int, max_pages: int):
        """Prints books whose number of pages is within a given range"""
        books_found = 0
        for book in self.books:
            if min_pages <= book.number_of_pages <= max_pages:
                books_found += 1
                print(book)
                print("------")
        if books_found == 0:
            print("No books found with a given number of pages.")

    def add_customer(self, customer):
        """Adds a customer to the library's list of customers"""
        self.customers.append(customer)

    def customer_by_id(self, customer_id: str):
        """Takes an ID number of a customer and returns a customer object if such exists in the customers list"""
        found = 0
        for customer in self.customers:
            if customer.get_id() == customer_id:
                found += 1
                return customer
        if found == 0:
            return 0

    def remove_customer(self, customer_id: str):
        """Remove a customer from the library's list of customers"""
        found = 0
        for customer in self.customers:
            if customer.get_id() == customer_id:
                found += 1
                self.customers.remove(customer)
        if found == 0:
            return 0

    def show_customers(self):
        """Prints the info of all the library's customers"""
        for customer in self.customers:
            print(customer)
            print("--------")

    def hire_employee(self, employee):
        """Puts a new employee object in the library's list of employees"""
        self.employees.append(employee)

    def employee_by_id(self, employee_id: str):
        """Takes an ID number of an employee and returns an employee object if such exists in the employees list"""
        found = 0
        for employee in self.employees:
            if employee.get_id() == employee_id:
                found += 1
                return employee
        if found == 0:
            return 0

    def fire_employee(self, employee_id: str):
        """Removes an employee object by its id from the library's list of employees"""
        found = 0
        for employee in self.employees:
            if employee.get_id() == employee_id:
                found += 1
                self.employees.remove(employee)
        if found == 0:
            return 0

    def show_employees(self):
        """Prints the info of all the library's employees"""
        for employee in self.employees:
            print(employee)
            print("--------")

    def get_utility_costs(self):
        """Returns monthly utility costs"""
        return self.__utility_costs

    def set_utility_costs(self, utility_costs: float):
        """Changes monthly utility costs"""
        self.__utility_costs = utility_costs

    def get_monthly_membership_fee(self):
        """Returns monthly membership fee"""
        return self.__membership_fee

    def change_monthly_membership_fee(self, fee: float):
        """Changes the monthly membership fee"""
        self.__membership_fee = fee

    def calculate_monthly_costs(self):
        """Calculates the total monthly costs of the library"""
        salary_costs = 0
        for employee in self.employees:
            salary_costs += employee.get_salary()
        total_monthly_costs = salary_costs + self.get_utility_costs()
        return total_monthly_costs

    def show_monthly_costs(self):
        """Prints current monthly costs breakdown"""
        print("CURRENT MONTHLY COSTS")
        print("=====================")
        print("Salary costs:")
        for i, employee in enumerate(self.employees):
            print(f"{i + 1}) Employee ID: {employee.get_id()} >> Monthly salary costs: {employee.get_salary()}")
        if len(self.employees) == 0:
            print(0)
        print(f"Utility costs: {self.get_utility_costs()}")
        print(f"Total monthly costs: {self.calculate_monthly_costs()}")

    def calculate_monthly_revenue(self):
        """Calculates monthly revenue of the library"""
        total_monthly_revenue = len(self.customers) * self.get_monthly_membership_fee()
        return total_monthly_revenue

    def show_monthly_revenue(self):
        """Prints current monthly revenue breakdown"""
        print("CURRENT MONTHLY REVENUE")
        print("=======================")
        print(f"Current monthly membership fee: {self.get_monthly_membership_fee()}")
        print(f"Current number of customers: {len(self.customers)}")
        print(f"Total monthly revenue: {self.calculate_monthly_revenue()}")

    def calculate_monthly_profit(self):
        """Calculates monthly profit or loss with the current customer count and workforce employed"""
        monthly_result = self.calculate_monthly_revenue() - self.calculate_monthly_costs()
        return monthly_result

    def show_monthly_profit(self):
        """Prints current monthly costs, revenue and the resulting profit or loss"""
        print("CURRENT MONTHLY PROFIT/LOSS")
        print("===========================")
        print(f"Current monthly costs: {self.calculate_monthly_costs()}")
        print(f"Current monthly revenue: {self.calculate_monthly_revenue()}")
        if self.calculate_monthly_profit() >= 0:
            print(f"Current monthly profit: {self.calculate_monthly_profit()}")
        else:
            print(f"Current monthly loss: {self.calculate_monthly_profit()}")
