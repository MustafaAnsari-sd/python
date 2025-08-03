# class is a blueprint or template. e.g form for exam that contains name, age , electives , fathter's name, etc
#object is an instance of a class. e.g. form filled by a student
class Employee:
    company = "Google"  # class variable, shared by all instances

    def get_salary(self):  # self is a reference to the current instance
        return 30000

# Object creation and method calls must be outside the class definition
e1 = Employee()  # creating an instance of the class Employee
print(e1.get_salary())  # calling the method get_salary on the instance e1

e2 = Employee()  # creating another instance of the class Employee
print(e2.get_salary())  # calling the method get_salary on the instance e2
