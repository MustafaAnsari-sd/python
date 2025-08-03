class product:
    brand = "dell" # this is a class attribute
    def __init__(self, name, price, quantity, brand):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.brand = brand
    
    def display(self):
        print(f"Product Name: {self.name}")
        print(f"Price: ₹{self.price}")
        print(f"Quantity: {self.quantity}")
    
    def total(self):
        total_price = self.price * self.quantity
        print(f"Total Price: ₹{total_price}")

prod1 = product("Laptop", 50000, 2, "HP")
print(prod1.brand)  # will always print instance attribute whenever present
# in above case it will print "HP" because it is an instance attribute
# if hp is not present then it will print class attribute "dell"

#object introspection
print(dir(prod1))  # will print all the attributes and methods of the object prod1
