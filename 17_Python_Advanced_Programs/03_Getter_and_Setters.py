class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def first_name(self):
        l = self.name.splt(' ')
        print(1)
        return l[0]

    def set_first_name(self, name):
        l = self.name.split(' ')
        new_name = f"{first} {l[1]}"    
        self.name = new_name

e = Employee("Isu", 50000)
e.projects = 6
print(e.projects)
e .set_first_name("Isuru")