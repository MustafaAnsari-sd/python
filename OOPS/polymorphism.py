#Polymorphism means many forms — same method name behaving differently in different classes.

# It comes in two main forms in Python:
# there are two types of polymorphism
#1) runtime (method overriding)
#e.g -
# class ClothingItem:
#     def show_info(self):
#         print("This is a generic clothing item.")

# class Jeans(ClothingItem):
#     def show_info(self):  # Overriding parent method
#         print("This is a pair of jeans.")


# # 2) polymorphism with funtions or loops
# for item in [ClothingItem(), Jeans()]:
#     item.show_info()  # Calls the appropriate version depending on object

class ClothingItem:
    def show_info(self):
        return "Generic clothing item"

class Tshirt(ClothingItem):
    def show_info(self):
        return "This is a T-shirt"

class Jeans(ClothingItem):
    def show_info(self):
        return "This is a pair of jeans"

# Step 3: Polymorphism in action
item1 = ClothingItem()
item2 = Tshirt()
item3 = Jeans()

items = [item1, item2, item3]

for item in items:
    print(item.show_info())

