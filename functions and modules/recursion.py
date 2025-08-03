#fibonaanci series
def fibonacci(n):
    # base case of recursion
    if(n == 0 or n==1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)

a =int(input("enter required term of fibonacci series: "))
print(fibonacci(a))



'''
fibonacci(6) can be split as follows:
fibonacci(5) + fibonacci(4)
fibonacci(5) can be split as follows:
fibonacci(4) + fibonacci(3) + fibonacci(4) 
fibonacci(4) can be split as follows:
fibonacci(3) + fibonacci(2)
fibonacci(3) can be split as follows: 
fibonacci(2) + fibonacci(1)
fibonacci(2) can be split as follows:
fibonacci(1) + fibonacci(0)

'''