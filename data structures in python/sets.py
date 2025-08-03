#s = {3,5,6,7,2}
#print(s,type(s))  # set is an unordered collection of unique elements

# SETS methods
'''
s = {3, 5, 6, 7, 2}
s.add(56)  # add an element to the set
print(s)
s.remove(3)  # remove an element from the set
print(s)
s.discard(8)  # discard an element from the set, does not raise an error if the element is not present
print(s)
s.pop() #remove random element from the set
print(s)
s.clear()  # clear the set
print(s)  # this will print an empty set
'''
# SETS operations
s1 = {3, 5, 6, 7, 2}
s2 = {5, 6, 8, 9, 10}
print(s1.union(s2))  # union of two sets
print(s1.intersection(s2))  # intersection of two sets
print(s1.difference(s2))  # difference of two sets
print(s1.symmetric_difference(s2))  # symmetric difference of two sets
print(s1.issubset(s2))  # check if s1 is a subset of s2
print(s1.issuperset(s2))  # check if s1 is a superset of s2
print(s1.isdisjoint(s2))  # check if s1 and s2 are disjiont sets
print(s1 == s2)  # check if s1 and s2 are equal
print(s1 != s2)  # check if s1 and s2 are not equal
