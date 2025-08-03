#tuples are similar to lists but they are immutable
# tuples are defined using parentheses
# we can use tuples to store data in a structured way
a = (1, 2, 3, 4, 5) #tuple
b = (1, 2, 3, 4, 5, "hello", True) #tuple with mixed data types
print(a) # we can access elements of a tuple using index
print(a[0]) # first element
# we should use tuples when we dont want our collection to accessibly change
print(a[1:4]) # elements from index 1 to 3

c = (6,) # this is a tuple with one element, we need to add a comma to make it a tuple
print(c) # this will print (6,)
# difference between list and tuple
# lists are mutable, tuples are immutable
# MUTUBALE means we can change the elements of a list, but we cannot change the elements of a tuple
print(a[1:]) # elements from index 1 to end