# a = input("enter a number ")
# print(a)
# a = input("enter first number ")
# a = int(a) # converting value of a into string
# print(a + 4)

# a = int(input("enter first number "))
# b = int(input("enter second number"))
# print(a+b)

# calculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Enter the operation to perform:")
print("For addition: +")
print("For subtraction: -")
print("For multiplication: *")
print("For division: /")

operation = input("Enter operation: ")

if operation == '+':
    print("Result:", a + b)
elif operation == '-':
    print("Result:", a - b)
elif operation == '*':
    print("Result:", a * b)
elif operation == '/':
    if b == 0:
        print("Error: Cannot divide by zero!")
    else:
        print("Result:", a / b)
else:
    print("Invalid operation!")
# End of calculator program