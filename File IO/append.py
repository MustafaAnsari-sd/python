#append to a file college.txt
# add age = 20
f = open("college.txt", "a")  # 'a' mode for appending
# Writing multiple lines to the file
string = '''
My college name saboo Siddiqui Engineering College,
I am currently in 3rd year of B.E. Computer Engineering.
I am an AIML engineering student.
I am currently learning Python and Flask.
I am also learning PostgreSQL, HTML, and CSS.
age =20
'''
f.write(string)
f.close()