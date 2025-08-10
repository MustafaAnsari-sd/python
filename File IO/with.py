with open("File IO/Mustafa.txt", "r") as f: # context manager
	content = f.read()
	print(content)
# no need to write f.close() because 'with' automatically closes the file
# This code reads the content of Mustafa.txt and prints it.
# Using 'with' ensures that the file is properly closed after its suite finishes, even if an exception is raised.
