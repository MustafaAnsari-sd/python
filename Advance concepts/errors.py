# try and except is use to handle errors in python 
while True:
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        print(f"The division is: {a / b}")

    except ValueError:
        print("Invalid input, please enter valid integers.")

    except ZeroDivisionError:
        print("Division by zero is not allowed. Please enter a non-zero number for the second input.")

    except Exception:
        print("Something went wrong. Please try again.")
