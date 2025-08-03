#there are many dunder methods in python 
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def __str__(self):
        return f"The name is {self.name} and the salary is {self.salary}"
    def __repr__(self):
        return f"name:"