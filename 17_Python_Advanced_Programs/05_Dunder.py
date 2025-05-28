class Employee:
    company = "Google" # This is a class attribute
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"The name is {self.name} and the salary is {self.salary}"
    
    def __repr__(self):
        return f"Employee(name={self.name}, salary={self.salary})"


e = Employee("Isu", 500000)
print(e.name, e.salary) # This will print the name and salary of the employee
print(str(e)) # This will call the __str__ method and print the string representation of the object
print(repr(e)) # This will call the __repr__ method and print the official string representation of the object. Mostly used by Developers for debugging purposes
