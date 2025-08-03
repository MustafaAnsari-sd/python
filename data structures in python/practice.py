# count even odd numbers in alist 
'''
def count_even_odd(num):
    even = 0
    odd = 0
    for i in num:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return {"even": even, "odd": odd}

# Input from user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Call the function
print(count_even_odd(numbers))
'''
# remove duplicates from alist
def remove_duplicates(my_list):
    result = []
    for item in my_list:
        if item not in result:
            result.append(item)
    return result  # <-- now outside the loop ✅

# Input from user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print(remove_duplicates(numbers))

    