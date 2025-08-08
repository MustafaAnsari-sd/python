# map, filter and reduce are higher order functions in python 
# They are used to apply a function to a sequence of elements.
'''
numbers = [1, 2,45, 65 ,66,5]
def square(x):
    return x*x

new = list(map(square, numbers))
print(new)
'''
# or
num = [12, 34, 54, 55, 9, 8]

new = list(map(lambda x: x*x, num))
print(new)