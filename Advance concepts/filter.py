def greater_than_ten(x):
    if x > 10:
        return True
    else:
        return False

num = [4, 44,54, 3,2,34, 45, 56]
new = list(filter(greater_than_ten, num))
print(new)