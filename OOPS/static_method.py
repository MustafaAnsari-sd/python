# A static method does not depend on either the class (cls) or the instance (self).

# It's used when you want a method that logically belongs to the class but doesn't need to access class or instance data
# class ClothingItem:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price

#     @staticmethod
#     def is_valid_price(price):
#         return price > 0

# Usage
# print(ClothingItem.is_valid_price(100))  # ✅ Works
# print(ClothingItem.is_valid_price(-50))  # ❌ Invalid price
# This code demonstrates the use of static methods in a class definition.
#the need of static method is to perform a task that does not require access to instance or class variables.
# Static methods are defined using the @staticmethod decorator.

class ClothingItem:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    
    @staticmethod
    def apply_discount(price, discount_percent):
        if discount_percent < 0 or discount_percent > 100:
            raise ValueError("Discount percent must be between 0 and 100")
        discount = price * (discount_percent / 100)
        return price - discount
# Usage
item1 = ClothingItem("Nike", 2000)
item2 = ClothingItem("Adidas", 1500)
print(f"Price after 10% discount: ₹{ClothingItem.apply_discount(item1.price, 10)}")  # ✅ Works
print(f"Price after 20% discount: ₹{ClothingItem.apply_discount(item2.price, 20)}")  # ✅ Works




