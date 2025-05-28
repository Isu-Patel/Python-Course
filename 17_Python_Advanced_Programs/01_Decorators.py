# Decorator is a function that takes a function, it creates a new function inside it's body(wrapper). Then it returns the new function.

def decorator(func):
    def wrapper():
        print("I am about to execute a function...")
        func()
        print("I have executed this function...")

def say_hello():
    print("Hello, Isu!")

# say_hello()
f = decorator(say_hello)  # This will return the wrapper function
f()  # This will execute the wrapper function, which in turn calls say_hello