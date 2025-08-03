'''
tu = (2,3,5)
a,b,c = tu # tuple unpacking 
print(a)
print(a,b,c) # we can unpack a tuple into multiple variables
'''
# tuple methods
tu = (2, 3, 5, 6, 7, 8, 9)
print(tu.count(2))  # count the number of occurrences of 2 in the tuple
print(tu.index(5))  # find the index of the first occurrence of 5 in the tuple
#tuple are faster than lists
# safe from unintendeed modifications
# we should use tuples when we dont want our collection to accessibly change
