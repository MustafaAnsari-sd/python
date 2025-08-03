'''class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount("Ravi", 1000)
acc.deposit(500)
print(acc.get_balance())  # ✅ Output: 1500
'''
# def frequency_count(text):
#     frequency = {}
#     words = text.split()  # splits by space
#     for word in words:
#         if word in frequency:
#             frequency[word] += 1
#         else:
#             frequency[word] = 1
#     return frequency

# # Get input from user
# sentence = input("Enter a sentence: ")
# print(frequency_count(sentence))

class ClothingItem:
    def __init__(self, brand, price, stock):
        self.brand = brand
        self.__price = price
        self.__stock = stock

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            raise ValueError("Price must be positive.")

    def get_stock(self):
        return self.__stock

    def set_stock(self, stock):
        if stock >= 0:
            self.__stock = stock
        else:
            raise ValueError("Stock must be non-negative.")

    def purchase(self, quantity):
        if quantity <= self.__stock:
            self.__stock -= quantity
            print(f"Purchased {quantity} items. Remaining stock: {self.__stock}")
        else:
            print("Not enough stock available.")
