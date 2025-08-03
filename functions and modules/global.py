z = 3 # global variable
def sum(a,b):
    print("hey i am summing")
    c = a + b
    global z #please modify the global variable z
    z = 0
    return c
print(sum(60 ,160))
print(z)