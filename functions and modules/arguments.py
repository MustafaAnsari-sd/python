def add(a,b, c=3):
    d = a+b+c
    return d
h = add(1,3,4)
print(h)
# since c has a default value, you can call add with just two arrguments 
h = add(1,3)
print(h)