#count vowels in a string
'''''
text = str(input("Enter a string: ")) 
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count +=1
print("Number of vowels in the string:", count)
'''

# check if a string is palindrome

'''
text = str(input("Enter a string: "))
 
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
'''
# reverse a string
text = "python"
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

print(reversed_text)


# 🔹 Fundamentals

# 1. Simple Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "*":
    print("Result:", num1 * num2)
elif op == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operator")

# 2. Area and Perimeter of Rectangle
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
print("Area:", length * breadth)
print("Perimeter:", 2 * (length + breadth))

# 3. Swap Two Numbers Without Temp Variable
a = int(input("Enter a: "))
b = int(input("Enter b: "))
a, b = b, a
print("After swapping: a =", a, ", b =", b)

# 4. Data Type Checker
val = input("Enter something: ")
print("As int:", int(val))
print("As float:", float(val))
print("As string:", str(val))

# 5. Even or Odd
n = int(input("Enter number: "))
print("Even" if n % 2 == 0 else "Odd")

# 🔹 Strings

# 6. Palindrome Checker
s = input("Enter a string: ")
print("Palindrome" if s == s[::-1] else "Not a palindrome")

# 7. Vowel Counter
s = input("Enter a string: ")
vowels = 'aeiouAEIOU'
count = sum(1 for char in s if char in vowels)
print("Vowels:", count)


# 8. Word Reverser
sentence = input("Enter sentence: ")
print(' '.join(word[::-1] for word in sentence.split()))

# 9. Character Frequency
s = input("Enter string: ")

for char in set(s):
    print(f"{char}: {s.count(char)}")

# 10. Remove Duplicates
s = input("Enter string: ")
result = ''
for char in s:
    if char not in result:
        result += char
print("Without duplicates:", result)

# 11. Longest Word
sentence = input("Enter sentence: ")
words = sentence.split()
longest = max(words, key=len)
print("Longest word:", longest)

# 12. Capitalize First Letter
s = input("Enter string: ")
print(s.title())

# 🔹 Control Flow

# 13. Grade Calculator
marks = int(input("Enter marks: "))
if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
else:
    grade = 'F'
print("Grade:", grade)

# 14. Leap Year
year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# 15. Age Category
age = int(input("Enter age: "))
text = "python"
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print(reversed_text)  # Output: nohtyp

# 16. Login System
username = "admin"
password = "1234"
user = input("Username: ")
passwd = input("Password: ")
if user == username and passwd == password:
    print("Login successful")
else:
    print("Login failed")

# 17. Rock-Paper-Scissors
import random
choices = ["rock", "paper", "scissors"]
user = input("Choose rock, paper or scissors: ").lower()
comp = random.choice(choices)
print("Computer chose:", comp)
if user == comp:
    print("Draw")
elif (user == "rock" and comp == "scissors") or (user == "scissors" and comp == "paper") or (user == "paper" and comp == "rock"):
    print("You win!")
else:
    print("You lose!")

# 🔹 Loops

# 18. Multiplication Table
n = int(input("Enter number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# 19. Factorial
n = int(input("Enter number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)

# 20. Fibonacci
n = int(input("Enter number of terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b

# 21. Sum of Digits
n = input("Enter number: ")
sum_digits = sum(int(d) for d in n)
print("Sum of digits:", sum_digits)

# 22. Prime Checker
n = int(input("Enter number: "))
if n < 2:
    print("Not prime")
else:
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")

# 23. Number Pattern
for i in range(1, 5):
    for j in range(1, i+1):
        print(j, end='')
    print()

# 24. Guess the Number
import random
num = random.randint(1, 10)
guess = -1
while guess != num:
    guess = int(input("Guess (1-10): "))
    if guess < num:
        print("Too low!")
    elif guess > num:
        print("Too high!")
print("Correct!")

# 25. Count Pos/Neg/Zero
pos = neg = zero = 0
while True:
    n = int(input("Enter number (0 to stop): "))
    if n == 0:
        break
    elif n > 0:
        pos += 1
    else:
        neg += 1
print("Positive:", pos, "Negative:", neg)











