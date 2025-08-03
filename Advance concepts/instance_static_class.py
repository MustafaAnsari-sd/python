class employee:
    company = 'microsoft'
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    #instance method(default)
    def info(self):

        inf = f"the name is {self.name} and the salary is {self.salary}"
        print(inf)
    
    #static method
    @staticmethod
    def sum(a, b): # no need to write self , this is advantage of static method

        return a+b
    #class method
    @classmethod
    def print_company(cls):
        print(cls.company)
    
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

e1 = employee("warner", 4000000)
e2 = employee("harry", 5000000)
e1.info()
e2.info()
print(employee.sum(5, 6))
# Accessing static method using instance
print(e1.sum(10, 20))
e1.print_company()
e1.change_company("google")
e1.print_company()
print(employee.company) # you can also print like this
print(e2.company) # you can also print like this
# Accessing class method using instance