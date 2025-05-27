class Employee:

    company = "Google" # This is a class attribut

    def __init__(self, salary, name, bond, company):
        self.salary = salary # Create an instance attribute of name salary and assign it with the salary
        self.name = name
        self.bond = bond
        self.company = company

    def get_salary(self):
        return self.salary

    def get_info(self):
        print(f"The name of the Employee is {self.name}.\nHis salary is {self.salary}.\nHe has been in the company for {self.bond} years")

e1 = Employee(50000, "Isu", 5, "Tesla")
print(e1.company) # This will always print instance attribute whenever present
print(Employee.company) # This will always prints the class attribute

# Object Introspection
# print(dir(e1))