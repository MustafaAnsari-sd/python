age = 14 # integer
name = "mustafa" # string
cgpa = 9.5 # float
name = "mustafa ansari "
# typecaste = int(name)
# print(typecaste) # This will raise an error because you cannot convert a string to an integer directly

# rule of defining a variable in Python
# 1) variable name must start with a letter(a-z, A-Z)or an underscore(_)
# 2) they can contain letters , numbers and underscore but not special character (eg - @)
# 3) variables name are case sensitive ( age and AGE are different)
# 4) avoid using python keywords (if , for , while , etc) as variable name

# python supports several built-in data types :
# 1) integer
# 2) float
# 3) strings 
# 4) boolean 
# 5) lists: ordered mutable collections (e.g , [1,2,3]).
# 6) tuples: ordered imutable collections (e.g, (1,2,3)).
# 7) sets: unordered collections of unique elements (e.g, {1, 2, 3}).
# 8) dictionaries: key- value pairs (e.g,{"name": "alice","age": 25}).

'''
print(age)
print(type(age))
print(name)
print(type(name))
print(cgpa)
print(type(cgpa))
'''

if 5 > 2:
 print("Five is greater than two!")
 # Spaces before print are called indentation
 name =input("Enter your name: ")
 age =int(input("Enter your age: "))
 print(f"Hello {name}, you are {age} years old.")
# The above code will take input from the user and print it
# The f-string is used to format the string with variables