def divide(a, b):

    try:
        c = a / b
        print(c)

    except Exception as e:
        print(e)

    # This is always executed, even if there is an error in the try block
    finally:
        print("This will always be executed, no matter what!")


a = int(input("Enter a number 1: "))
b = int(input("Enter a number 2: "))
divide(a, b)
# The finally block is used to execute code that must run whether an exception occurs or not.
# Example: closing a file after reading it, regardless of whether an error occurred during the read operation.
# In this case, the finally block is used to print a message that indicates it will always be executed.