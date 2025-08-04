#there are many dunder methods in python 
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def __str__(self):
        return f"The name is {self.name} and the salary is {self.salary}"
    def __repr__(self):
        return f"name: {self.name},salary: {self.salary}"
    def __len__(self):
        return len(self.name)

# __str__ is used for user-friendly string representation
# __repr__ is used for debugging and development, providing a detailed string representation
# Example usage
emp = Employee("John", 50000)
print(str(emp))   # Output: The name is John and the salary is 50000
print(repr(emp))  # Output: name: John, salary: 50000
print(len(emp))   # Output: 4 (length of the name "John")