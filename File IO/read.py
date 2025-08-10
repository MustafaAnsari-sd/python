#file allows persistent storage of data
#write, append, read
f = open("File IO/Mustafa.txt", "r")

content = f.read()
print(content)
f.close()
