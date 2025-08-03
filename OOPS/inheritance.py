# class Animal: # parent class(super class)
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         print(" generic animal sound")

# class dog(Animal): #this is how inheritance works in python
#     def speak(self):
#         print("woof")

# d = dog("tommy")
# d.speak()
'''
class ClothingItem:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_info(self):
        print(f"Brand: {self.brand}, Price: ₹{self.price}")

class TShirt(ClothingItem):  # Inheriting
    def __init__(self, brand, price, sleeve_type):
        super().__init__(brand, price)   # Call parent constructor
        self.sleeve_type = sleeve_type

    def show_details(self):
        self.show_info()
        print(f"Sleeve Type: {self.sleeve_type}")
'''
class ClothingItem:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_info(self):
        return f"Brand: {self.brand}, Price: ₹{self.price}"

class Jeans(ClothingItem):
    def __init__(self, brand, price, fit_type):
        super().__init__(brand, price)
        self.fit_type = fit_type

    def show_details(self):
        info = self.show_info()
        return f"{info}\nFit Type: {self.fit_type}"

# Object creation
j1 = Jeans("Levi's", 2499, "Slim")

# Output
print(j1.show_details())
