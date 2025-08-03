import math
print(math.sqrt(16))
# there are two types of modules:
# 1. built-in modules: these are modules that come with Python, such as math, os, sys, etc.
# 2. user-defined modules: these are modules that you create yourself, such as the one we are creating here
# to use a module, you need to import it using the import statement


#https://docs.python.org/3/py-modindex.html - list of all built-in modules
import os 
print(os.getcwd())  # Get the current working directory
import requests
r = requests.get("https://www.microsoft.com")
print(r.text)  # Print the HTML content of the page
# You can also import specific functions or classes from a module
