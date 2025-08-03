#"Print all even numbers from 1 to 100 using a while loop, but skip numbers divisible by 10."
# i = 0
# while i<=100:
#     if i % 2 == 0 and i % 10 != 0:
#         print(i)
#     i += 1

#"Take a string from the user and reverse it without using slicing ([::-1]) or reversed() function."
# text = input("Enter a string: ")
# reversed_string = ""

# for char in text:
#     reversed_string = char + reversed_string

# if reversed_string == text:
#     print("The string is a palindrome")
# else:
#     print("The string is not a palindrome"

# Sentence = input("Enter a sentence: ")
# record = {}
# for char in Sentence:
#     if char not in record:
#         record[char] = 1
#     else:
#         record[char] += 1

fibo = int(input("Enter number of terms:"))
f1, f2 = 0, 1
print("Fibonacci Series:")
for i in range(fibo):
    print(f1, end=' ')
    f1, f2 = f2, f1 + f2
    



