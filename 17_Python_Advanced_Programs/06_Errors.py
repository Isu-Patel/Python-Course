# while True:
#     try:
#         a = int(input("Enter a number 1: "))
#         b = int(input("Enter a number 2: "))

#         print(f"The division of {a / b}")

#     except ValueError:
#         print("Please dont perform bad typecasts!")

#     except ZeroDivisionError:
#         print("Please dont dicide by 0!")

#     except Exception as e:
#         print("Unknown Error Occured!", e)

a = int(input("Enter a number 1: "))
b = int(input("Enter a number 2: "))

if b == 0:
    raise ValueError("You cannot divide by zero!")

print(f"The division of {a / b}")