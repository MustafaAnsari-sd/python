#write to a file college.txt
f = open("college.txt", "w")
# Writing multiple lines to the file
string = '''
My college name saboo Siddiqui Engineering College,
I am currently in 3rd year of B.E. Computer Engineering.
I am an AIML engineering student.
I am currently learning Python and Flask.
I am also learning PostgreSQL, HTML, and CSS.
'''
f.write(string)
f.close()