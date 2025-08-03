# class Product:
#     discount_percent = 10  # class variable shared by all

#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def apply_discount(self):
#         discount = self.price * (Product.discount_percent / 100)
#         return self.price - discount

# p1 = Product("Shoes", 2000)
# p2 = Product("T-Shirt", 1000)

# print(f"{p1.name} after discount: ₹{p1.apply_discount()}")
# print(f"{p2.name} after discount: ₹{p2.apply_discount()}")
# # This code demonstrates the use of class variables in a class definition.
class Student:
    total_students = 0  # class variable to keep track of total students
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        Student.total_students += 1
    def display_info(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}")
    
# Create student objects
std1 = Student("Rahul", "101")
std2 = Student("Sneha", "102")
std1.display_info()
std2.display_info()
print(f"Total Students: {Student.total_students}")  # Accessing class variable
