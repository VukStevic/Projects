from library_class import Library
from customer_class import Customer
from book_class import Book
from employee_class import Employee


def return_or_quit() -> str:
    """Asks user to either return to the main menu or quit the program,
       prints a message in case of an invalid input."""
    user_answer = input("Return/Quit? >> ").lower()
    user_options = ["return", "quit"]
    while user_answer not in user_options:
        print("Invalid input.")
        user_answer = input("Return/Quit? >> ").lower()
    return user_answer


def is_float(num: str):
    """Checks if a given string can be turned into a float"""
    try:
        float(num)
        return True
    except ValueError:
        return False


library = Library()
library.read_books_from_file("books.txt")
library.read_employees_from_file("employees.txt")

main_menu = """
========================== LIBRARY MANAGER ==========================

>> For each option type the letter representing it:

   BOOK OPTIONS
   a) Show all the books in the library's inventory
   b) Show all the books that are currently available and the number of copies available
   c) Show all lent out books, who they were lent to and when, and whether the customer exceeded the deadline or not
   d) Selection of books by the title
   e) Selection of books by the author
   f) Selection of books by genre
   g) Selection of books by a publication year
   h) Selection of books within a given range of publication years
   i) Selection of books by the number of pages
   j) Add a new book to the library
   k) Remove a book from the library
   
   CUSTOMER OPTIONS
   l) Adding a new customer to the library
   m) Lending a book to the customer
   n) Checking return deadlines
   o) Receiving a book back from the customer
   p) Removing a customer from the library
   
   EMPLOYEE OPTIONS
   q) Hire an employee
   r) Change employee's salary
   s) Fire an employee
   
   FINANCES
   t) Increase/decrease monthly membership fee
   u) Calculate monthly costs
   v) Calculate monthly revenue
   w) Calculate monthly profit/loss
   ---------------------------------------
   x) Exit program                

>>> """

if __name__ == '__main__':

    answer = input(main_menu).lower()

    options = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "o", "p", "q",
               "r", "s", "t", "u", "v", "w", "x"]

    while answer != "x":
        if answer == "a":
            print("LIST OF BOOKS OWNED BY THE LIBRARY")
            print("==================================")
            library.show_all_books()
            answer = return_or_quit()
            if answer == "return":
                answer = input(main_menu).lower()
            elif answer == "quit":
                break

        elif answer == "b":
            print("LIST OF CURRENTLY AVAILABLE BOOKS")
            print("=================================")
            library.show_available_books()
            answer = return_or_quit()
            if answer == "return":
                answer = input(main_menu).lower()
            elif answer == "quit":
                break

        elif answer == "c":
            print("LIST OF BOOKS CURRENTLY LENT OUT TO CUSTOMERS")
            print("=============================================")
            library.show_lent_books()
            answer = return_or_quit()
            if answer == "return":
                answer = input(main_menu).lower()
            elif answer == "quit":
                break

        elif answer == "d":
            title = input("Enter a title: >> ").lower()
            if library.book_by_title(title) == 0:
                print("No book with a given title.")
            else:
                print("BOOKS BY THE TITLE")
                print("==================")
                library.books_by_title(title)
            answer = return_or_quit()
            if answer == "return":
                answer = input(main_menu).lower()
            elif answer == "quit":
                break

        elif answer == "e":
            author = input("Enter an author: >> ").lower()
            print("BOOKS BY THE AUTHOR")
            print("===================")
            library.books_by_author(author)
            answer = return_or_quit()
            if answer == "return":
                answer = input(main_menu).lower()
            elif answer == "quit":
                break

        elif answer == "f":
            genre = input("Enter a genre: >> ").lower()
            print("BOOKS OF SELECTED GENRE")
            print("=======================")
            library.books_by_genre(genre)
            answer = return_or_quit()
            if answer == "return":
                answer = input(main_menu).lower()
            elif answer == "quit":
                break

        elif answer == "g":
            year = input("Enter a publication year: >> ")
            while not year.isnumeric():
                print("Only numeric values allowed.")
                year = input("Enter a publication year: >> ")
            year = int(year)
            print("BOOKS PUBLISHED IN A SELECTED YEAR")
            print("==================================")
            library.books_by_year(year)
            answer = return_or_quit()
            if answer == "return":
                answer = input(main_menu).lower()
            elif answer == "quit":
                break

        elif answer == "h":
            start_year = input("Enter the starting year: >> ")
            while not start_year.isnumeric():
                print("Only integers allowed.")
                start_year = input("Enter the starting year: >> ")
            start_year = int(start_year)
            ending_year = input("Enter the ending year: >> ")
            while not ending_year.isnumeric():
                print("Only integers allowed.")
                ending_year = input("Enter the ending year: >> ")
            ending_year = int(ending_year)
            print("BOOKS PUBLISHED IN A SELECTED YEAR PERIOD")
            print("=========================================")
            library.books_by_period(start_year, ending_year)
            answer = return_or_quit()
            if answer == "return":
                answer = input(main_menu).lower()
            elif answer == "quit":
                break

        elif answer == "i":
            min_pages = input("Enter the minimum number of pages: >> ")
            while not min_pages.isnumeric():
                print("Only integers allowed.")
                min_pages = input("Enter the minimum number of pages: >> ")
            min_pages = int(min_pages)
            max_pages = input("Enter the maximum number of pages: >> ")
            while not max_pages.isnumeric():
                print("Only integers allowed.")
                max_pages = input("Enter the maximum number of pages: >> ")
            max_pages = int(max_pages)
            print("BOOKS BY A SELECTED PAGE COUNT RANGE")
            print("====================================")
            library.books_by_number_of_pages(min_pages, max_pages)
            answer = return_or_quit()
            if answer == "return":
                answer = input(main_menu).lower()
            elif answer == "quit":
                break

        elif answer == "j":
            title = input("Enter the book's title: >> ").title()
            author = input("Enter the author's name and surname: >> ").title()
            year = input("Enter the publication year: >> ")
            while not year.isnumeric():
                print("Only integers allowed.")
                year = input("Enter the publication year: >> ")
            year = int(year)
            genre = input("Enter the book's genre: >> ").lower()
            number_of_pages = input("Enter the number of pages: >> ")
            while not number_of_pages.isnumeric():
                print("Only integers allowed.")
                number_of_pages = input("Enter the number of pages: >> ")
            number_of_pages = int(number_of_pages)
            library.add_books(Book(title, author, year, genre, number_of_pages))
            print("Book successfully added.")
            answer = return_or_quit()
            if answer == "return":
                answer = input(main_menu).lower()
            elif answer == "quit":
                break

        elif answer == "k":
            title = input("Enter the book's title: >>  ")
            if library.remove_books(title) == 0:
                print("No books with a given title.")
            else:
                print("Book successfully removed.")
            answer = return_or_quit()
            if answer == "return":
                answer = input(main_menu).lower()
            elif answer == "quit":
                break

        elif answer == "l":
            name = input("Enter the customer's name: >> ")
            surname = input("Enter the customer's surname: >> ")
            id_num = input("Enter the customer's ID number: >> ")
            cellphone_number = input("Enter the customer's cellphone number: >> ")
            landline_number = input("Enter the customer's landline number: >> ")
            library.add_customer(Customer(name, surname, id_num, cellphone_number, landline_number))
            print("Customer successfully added.")
            answer = return_or_quit()
            if answer == "return":
                answer = input(main_menu).lower()
            elif answer == "quit":
                break

        elif answer == "m":
            customer_id = input("Enter the customer's ID number: >> ")
            if library.customer_by_id(customer_id) == 0:
                print("No customer with a given ID number.")
            else:
                customer = library.customer_by_id(customer_id)
                book_title = input("Enter the book title: >> ").lower()
                customer.borrow(library, book_title)
            answer = return_or_quit()
            if answer == "return":
                answer = input(main_menu).lower()
            elif answer == "quit":
                break

        elif answer == "n":
            customer_id = input("Enter a customer's ID number: >> ")
            customer = library.customer_by_id(customer_id)
            if customer == 0:
                print("No customer with a given ID number.")
            else:
                title = input("Enter the book's title: >>  ")
                if library.book_by_title(title) == 0:
                    print("No book with a given title.")
                else:
                    if customer.is_within_deadline(title) == 0:
                        print("Customer either already returned the book or hasn't borrowed it yet.")
                    else:
                        # print(customer.is_within_deadline(title))
                        print("Within deadline" if customer.is_within_deadline(title) else print("Deadline exceeded."))
            answer = return_or_quit()
            if answer == "return":
                answer = input(main_menu).lower()
            elif answer == "quit":
                break

        elif answer == "o":
            customer_id = input("Enter the customer's ID number: >> ")
            if library.customer_by_id(customer_id) == 0:
                print("No customer with a given ID number.")
            else:
                customer = library.customer_by_id(customer_id)
                book_title = input("Enter the book title: >> ").lower()
                if library.book_by_title(book_title) == 0:
                    print("No book with a given title.")
                else:
                    customer.return_book(library, book_title)
            answer = return_or_quit()
            if answer == "return":
                answer = input(main_menu).lower()
            elif answer == "quit":
                break

        elif answer == "p":
            customer_id = input("Enter a customer's ID number: >> ")
            if library.customer_by_id(customer_id) == 0:
                print("No customer with a given ID number.")
            else:
                library.remove_customer(customer_id)
                print("Customer successfully removed.")
            answer = return_or_quit()
            if answer == "return":
                answer = input(main_menu).lower()
            elif answer == "quit":
                break

        elif answer == "q":
            name = input("Enter the employee's name: >> ")
            surname = input("Enter the employee's surname: >> ")
            id_num = input("Enter the employee's ID number: >> ")
            cellphone_number = input("Enter the employee's cellphone number: >> ")
            landline_number = input("Enter the employee's landline number: >> ")
            position = input("Enter the employee's position: >> ")
            salary = input("Enter the employee's monthly salary: >> ")
            while not salary.isnumeric():
                print("Only integers allowed.")
                salary = input("Enter the employee's monthly salary: >> ")
            salary = int(salary)
            library.hire_employee(Employee(name, surname, id_num, cellphone_number, landline_number, position, salary))
            print("Employee successfully hired.")
            answer = return_or_quit()
            if answer == "return":
                answer = input(main_menu).lower()
            elif answer == "quit":
                break

        elif answer == "r":
            employee_id = input("Enter employee's ID number: >> ")
            if library.employee_by_id(employee_id) == 0:
                print("No employee with a given ID number.")
            else:
                new_salary = input("Enter new monthly salary: >> ")
                while not new_salary.isnumeric():
                    print("Only integers allowed.")
                    new_salary = input("Enter new monthly salary: >> ")
                new_salary = int(new_salary)
                employee = library.employee_by_id(employee_id)
                employee.set_salary(new_salary)
                print("Salary updated.")
            answer = return_or_quit()
            if answer == "return":
                answer = input(main_menu).lower()
            elif answer == "quit":
                break

        elif answer == "s":
            employee_id = input("Enter employee's ID number: >> ")
            if library.employee_by_id(employee_id) == 0:
                print("No employee with a given ID number.")
            else:
                library.fire_employee(employee_id)
                print("Employee fired.")
            answer = return_or_quit()
            if answer == "return":
                answer = input(main_menu).lower()
            elif answer == "quit":
                break

        elif answer == "t":
            new_fee = input("Enter the new monthly membership fee: >> ")
            while not new_fee.isnumeric() and not is_float(new_fee):
                print("Only numeric values allowed.")
                new_fee = input("Enter the new monthly membership fee: >> ")
            new_fee = float(new_fee)
            library.change_monthly_membership_fee(new_fee)
            print("Monthly membership fee successfully changed.")
            answer = return_or_quit()
            if answer == "return":
                answer = input(main_menu).lower()
            elif answer == "quit":
                break

        elif answer == "u":
            library.show_monthly_costs()
            answer = return_or_quit()
            if answer == "return":
                answer = input(main_menu).lower()
            elif answer == "quit":
                break

        elif answer == "v":
            library.show_monthly_revenue()
            answer = return_or_quit()
            if answer == "return":
                answer = input(main_menu).lower()
            elif answer == "quit":
                break

        elif answer == "w":
            library.show_monthly_profit()
            answer = return_or_quit()
            if answer == "return":
                answer = input(main_menu).lower()
            elif answer == "quit":
                break

        elif answer == "x":
            break

        else:
            print("Invalid input.")
            answer = input(main_menu).lower()

    print("Program ended.")
