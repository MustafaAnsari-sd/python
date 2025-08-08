# try and except is use to handle errors in python 
# while True:
#     try:
#         a = int(input("Enter a number: "))
#         b = int(input("Enter another number: "))
#         print(f"The division is: {a / b}")

#     except ValueError:
#         print("Invalid input, please enter valid integers.")

#     except ZeroDivisionError:
#         print("Division by zero is not allowed. Please enter a non-zero number for the second input.")

#     except Exception:
#         print("Something went wrong. Please try again.")

# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# if b == 0:
#     raise ValueError("please dont divide by zero")
# print(f"The division is: {a / b}")
# This code will raise a ValueError if the second number is zero.
# This is a simple example of raising an exception in Python.
# try :
#     a = 345/10
# except Exception as e:
#     print(e)

# else:
#     print("hey I am good ")
# # The else block will execute if no exceptions are raised in the try block.

def divide(a,b):
    try:
        c= a/b
        print(c)
        return c
    except Exception as e:
        print(e)
        return None
    finally:
        print("this will always executed")

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
divide(a,b)
# The finally block will always execute, regardless of whether an exception was raised or not.
# This is useful for cleanup actions, such as closing files or releasing resources.
# The try block contains the code that may raise an exception.
# The except block handles the exception if it occurs.
# The else block executes if no exceptions were raised in the try block.
# The finally block executes regardless of whether an exception was raised or not.