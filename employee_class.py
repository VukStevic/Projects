from customer_class import Customer


class Employee(Customer):
    def __init__(self, name: str, surname: str, id_num: str, cellphone_number: str,
                 landline_number: str, position: str, salary: int):
        super().__init__(name, surname, id_num, cellphone_number, landline_number)
        self.__position = position
        self.__salary = salary

    def __str__(self):
        return f"Name: {self.name}\nSurname: {self.surname}\nPosition: {self.get_position()}\n" \
               f"Salary: {self.get_salary()}\nID number: {self.get_id()}\n" \
               f"Cellphone number: {self.cellphone_number}\nLandline number: {self.landline_number}"

    def get_position(self):
        """Returns employee's position"""
        return self.__position

    def set_position(self, position: str):
        """Sets employee's position"""
        self.__position = position

    def get_salary(self):
        """Returns employee's salary"""
        return self.__salary

    def set_salary(self, salary: int):
        """Sets employee's salary"""
        self.__salary = salary
