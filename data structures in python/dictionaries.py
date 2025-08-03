# dictionaries store data in key-value pairs
# dictionaries are unordered, mutable, and allow duplicate elements
# we use dictionaries to store data in a structured way
marks = {"harry": 45, "ron": 56, "hermione": 78, "draco": 90}  # dictionary
print(marks)  # print the dictionary
print(marks["harry"])  # print the value of the key "harry"
# in dictionaries key values are hashable, so we can use strings, numbers, and tuples as keys
marks["ron"] = 55  # update the value of the key "ron"
print(marks)  # print the updated dictionary
print(marks.keys())  # print the keys of the dictionary
print(marks.values())  # print the values of the dictionary
marks.clear()  # clear the dictionary
print(marks)  # print the empty dictionary
