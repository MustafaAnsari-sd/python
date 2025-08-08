# functools is a module that provides higher-order functions and it is inbuilt in Python.
from functools import reduce
numbers = [1, 3, 4,5, 6,33]

def sum(x,y):
    return x+y

c =reduce(sum, numbers)
print(c)
# The reduce function applies the sum function cumulatively to the items of the numbers list.
# It reduces the list to a single value, which is the sum of all elements in the list.