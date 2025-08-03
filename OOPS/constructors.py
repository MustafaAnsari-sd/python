'''
class BankAccount:
    # Constructor
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    # Method to display account details
    def show_account(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ₹{self.balance}")

    # Method to deposit money
    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited. New balance is ₹{self.balance}")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn. Remaining balance is ₹{self.balance}")
        else:
            print("Insufficient balance!")

# Create bank account objects
acc1 = BankAccount("Rahul", 5000)
acc2 = BankAccount("Sneha", 10000)

# Use methods
acc1.show_account()
acc1.deposit(2000)
acc1.withdraw(3000)

print("------")

acc2.show_account()
acc2.withdraw(12000)
'''
'''
class student:
    def __init__(self, name, sub1, sub2, sub3):
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
    def display(self):
        print(f"name: {self.name}")
        print(f"sub1: {self.sub1}")
        print(f"sub2: {self.sub2}")
        print(f"sub3: {self.sub3}")
    def average(self):
        avg = (self.sub1 + self.sub2 + self.sub3)/3
        print(f"average: {avg}")
    def grading(self):
        avg = (self.sub1 + self.sub2 + self.sub3)/3
        if avg >= 90:
            print("Grade: A")
        elif avg >= 80:
            print("Grade: B")
        elif avg >= 70:
            print("Grade: C")
        elif avg >= 60:
            print("Grade: D")
        else:
            print("Grade: F")
    
std1 = student("Rahul", 90, 80, 70)
std2 = student("Sneha", 85, 75, 95)
std1.display()
std1.average()
std2.display()
std2.average()
std1.grading()
std2.grading()
'''
class product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def display(self):
        print(f"Product Name: {self.name}")
        print(f"Price: ₹{self.price}")
        print(f"Quantity: {self.quantity}")
    
    def total(self):
        total_price = self.price * self.quantity
        print(f"Total Price: ₹{total_price}")

prod1 = product("Laptop", 50000, 2)
prod2 = product("Mobile", 20000, 3)
prod1.display()
prod1.total()
prod2.display()
prod2.total()
# constructor is called when an object is created, it initializes the object's attributes
# methods are functions defined inside a class that operate on the object's attributes
# they can be called on the object to perform actions or calculations related to that object
# constructor is used to initialize the object's attributes when the object is created