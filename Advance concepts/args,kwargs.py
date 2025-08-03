# *args captures any number of positional arguments as tuple
# **kwargs captures any number of keyword arguments as dictionary
'''
def add(*args):
    print(args)  # args is a tuple
    print("sum:", sum(args))

add(1, 2, 3)  # Output: (1, 2, 3) sum: 6
add(4, 5, 6, 7, 8)  # Output: (4, 5, 6, 7, 8) sum: 30
add(1,3)

def display_info(**kwargs):
    print(kwargs)

display_info(name="Mustafa", age=20, city="Mumbai")
display_info(name="Aaliyah", age=22, city="Mumbai", profession="Data Scientist")
'''
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper
@log_call
def divide(a,b):
    return a/b
divide(10, 2)  # Calling divide with args: (10, 2) and kwargs: {}
    