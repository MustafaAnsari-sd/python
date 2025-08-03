#we use data structures in python to store data in a structured way 
#we will use lists, tuples, sets and dictionaries to store data in a structured way
# list are ordered, mutable, and allow duplicate elements
# tuple are ordered, immutable, and allow duplicate elements
# set are unordered, mutable, and do not allow duplicate elements
# dictionary are unordered, mutable, and allow duplicate elements
# we will use these data structures to store data in a structured way
marks = [43, 56, 43, 45, 90, 78] #list
mixed = [43, 56, 43, 45, 90, 78, "hello", True] #list with mixed data types
print(marks)# we can access elements of a list using index
print(marks[0]) # first element 
print(marks[3])
#we can do slicing in lists
print(marks[1:4]) # elements from index 1 to 3