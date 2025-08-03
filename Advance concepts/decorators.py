# deocorators is a function that takes a function, it creates a new function inside its body(wrapper).then it returns that new function
'''
def decorator(func):
    def wrapper():
        print("iam about to execute the function")
        func()
        print("iam have executed this function")
    return wrapper

@decorator    
def say_hello():
    print("hello buddy")

say_hello()
'''
'''

def loading_decorator(func):
    def wrapper():
        print("Loading...")
        func()
        print("Done.")
    return wrapper

@loading_decorator
def task1():
    print("Task 1 running...")

@loading_decorator
def task2():
    print("Task 2 running...")

task1()
task2()
()# This code defines a decorator that adds loading messages before and after the execution of the decorated functions.
'''

#Create a decorator that counts how many times a function has been called, and prints the count each time
'''def count_calls(func):
    count = 0  # counter variable

    def wrapper():
        nonlocal count  # allows us to modify the outer 'count' variable
        count += 1
        print(f"Function has been called {count} times")
        func()
    
    return wrapper

@count_calls
def greet():
    print("Hello!")

greet()
greet()
greet()
        
'''
'''

def run_once(func):
    has_run = False  # This should be remembered across calls

    def wrapper():
        nonlocal has_run  # Let us modify 'has_run' from outer scope
        if not has_run:
            func()
            has_run = True
        else:
            print("Access Denied: This function can be called only once.")

    return wrapper

@run_once
def start():
    print("Welcome!")

start()
start()

'''

# Create a decorator that prints the name of the function before it runs.
# def show_function_name(func):
#     def wrapper():
#         print(f"Running function: {func.__name__}")  # Print the function name
#         func()  # Call the original function
#     return wrapper

# @show_function_name
# def say_hello():
#     print("Hello, world!")

# say_hello()
# Decorator is a function that takes another function as input, adds some functionality to it, and returns a new function — without modifying the original one.
# It's used when you want to "wrap" behavior around a function, like logging, timing, checking authentication, etc.
# def decorator_function(original_function):
#     def wrapper_function():
#         print("Wrapper executed before", original_function.__name__)
#         original_function()
#         print("Wrapper executed after", original_function.__name__)
#     return wrapper_function
# @decorator_function
# def say_hello():
#     print("Hello!")

# say_hello()


def my_decorator(func):
    def wrapper():
        print(">>> Something BEFORE")
        func()  # call the original function
        print(">>> Something AFTER")
    return wrapper

@my_decorator
def greet():
    print("Hello, World!")
greet()