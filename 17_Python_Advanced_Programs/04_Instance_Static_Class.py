class Employee:
    company = "Google" # This is a class attribute

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Instance method (default)
    def print_info(self):
        info = f"The name is {self.name} and the salary is {self.salary}"
        print(info)

    # Static Method
    @staticmethod
    def sum(a, b):
        return a + b
    
    # Class Methods
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company


e1 = Employee("Isu", 500000)
e2 = Employee("Atul", 250000)
# e3 = Employee("Shashikant", 1000000)
# print(Employee.company)  # This will always print the class attribute
# print(e1.company) # This will always print the instance attribute whenever present
# e1.print_info()  # This will print the info of e1
# e2.print_info()  # This will print the info of e2

# print(e2.sum(10, 24))

print(Employee.company) # This will print the company name from the class attribute
e1.change_company("Apple") # This will change the company name using the class method
print(Employee.company) # This will print the updated company name