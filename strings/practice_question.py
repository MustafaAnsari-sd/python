#swap two numbers without using a third variable 
'''
a = int(input("enter first number: "))
b = int(input("enter second number: "))
print("Before swapping: a =", a, ", b =", b)
a, b = b, a
print("After swapping: a =", a, ", b =", b)
'''

#print the sum of numbers from 1 to n
n = int(input("Enter a number: "))
sum_of_numbers = sum(range(1, n + 1))
print("Sum of numbers from 1 to", n, "is:", sum_of_numbers)
