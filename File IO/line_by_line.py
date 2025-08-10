# read any file line by line
f = open("File IO/Mustafa.txt", "r")
for line in f:
    print(line.strip())  # strip() removes leading/trailing whitespace
f.close()
# This code reads a file named Mustafa.txt line by line and prints each line without leading or trailing whitespace.
#use for reading large files effectively