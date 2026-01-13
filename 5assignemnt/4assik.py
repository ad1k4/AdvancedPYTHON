# 1. Create a base class Employee
class Employee:
    def __init__(self, name, salary):
        self.name = name
        # Private attribute (using __ to make it private)
        self.__salary = salary  

    def get_salary(self):
        return self.__salary

    def get_role(self):
        return "Employee"

# 2. Create a child class Manager
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        # Inherits from Employee
        super().__init__(name, salary)
        self.bonus = bonus

    def get_role(self):
        # Overrides get_role()
        return "Manager"

    def get_bonus(self):
        # Adds a method get_bonus()
        return self.bonus

# 3. Write a function that accepts a list and prints role/salary
def print_employee_details(employees):
    print("--- Employee Report ---")
    for emp in employees:
        role = emp.get_role()
        salary = emp.get_salary()
        print(f"Role: {role} | Name: {emp.name} | Salary: {salary}")

# Execution block
if __name__ == "__main__":
    # Creating objects
    emp1 = Employee("Alice", 3000)
    mgr1 = Manager("Bob", 5000, 1000)

    # Creating a list of Employee objects
    staff_list = [emp1, mgr1]
    
    # Calling the function
    print_employee_details(staff_list)