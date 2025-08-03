# #rotate list to right by k times
# def rotate_list(my_list, k):
#     n = len(my_list)
#     k = k % n  # handle k > n
#     rotated = []

#     for i in range(n - k, n):
#         rotated.append(my_list[i])
#     for i in range(n - k):
#         rotated.append(my_list[i])

#     return rotated

# # Input section
# inp = input("Enter the list elements separated by space: ").split()
# times = int(input("Enter number of rotations: "))

# # Convert input strings to integers (optional, based on use case)
# inp = [int(x) for x in inp]

# # Output
# print("Rotated List:", rotate_list(inp, times))

# items = ["Shirt", "Shoes", "Watch", "Bag"]
# for i in range(len(items)):
#     print(f"Item {i+1}: {items[i]}")
# email = "mustafaansari@gmail.com"
# username = email.split("@")[0]
# domain = email.split("@")[1]

# print(f"Username: {username}, Domain: {domain}")
# coordinates = (12.5, 77.6)
# print(f"Latitude: {coordinates[0]}")
# class Employee:
#     def __init__(self, name, role, salary):
#         # Assign values to object
#         self.name = name
#         self.role = role
#         self.salary = salary

#     def display_info(self):
#         print(f"{self.name} is a {self.role} earning ₹{self.salary}")

# # Create objects
# emp1 = Employee("Mustafa", "Python Developer", 80000)
# emp2 = Employee("Aaliyah", "ML Engineer", 95000)

# emp1.display_info()
# emp2.display_info()


# class book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price
#     def get_info(self):
#         return f"Title: {self.title}, Author: {self.author}, Price: ₹{self.price}"
   


# book1 = book("Python Programming", "John Doe", 499)
# book2 = book("Data Science Handbook", "Jane Smith", 599)
# print(book1.get_info())
# print(book2.get_info())
 
class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited. New balance is ₹{self.balance}")
    def withhdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn. Remaining balance is ₹{self.balance}")
        else:
            print("Insufficient balance!")
    def get_balance(self):
        return self.balance
    def get_info(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: ₹{self.balance}"
# Create bank account objects
acc1 = BankAccount("123456789", "Rahul", 5000)
acc2 = BankAccount("987654321", "Sneha", 10000)
# Use methods
print(acc1.get_info())
acc1.deposit(2000)
acc1.withhdraw(3000)
