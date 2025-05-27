class Animal: # Parent Class (SuperClass)
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Speaking Now...")

class Dog(Animal): # This is how inheritance is done in Python
    def speak(self):
        super().speak() # We are using the speak function of the parent class
        print("Woof! Woof!")

a = Animal("Dog")
a.speak()
d = Dog("Bruno")
d.speak()