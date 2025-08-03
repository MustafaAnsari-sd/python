# class methods are methods that are bound to the class and not the instance of the class.
#they are use for basically updating  , keyword is cls just like self
# use @classmethod decorator to define a class method
# class Student:
#     def __init__(self, name, roll_no):
#         self.name = name
#         self.roll_no = roll_no

#     @classmethod
#     def from_string(cls, student_str):
#         name, roll_no = student_str.split("-")
#         return cls(name, roll_no)  # creating and returning object

# # Create using normal constructor
# s1 = Student("Ali", "103")

# # Create using class method
# s2 = Student.from_string("Zoya-104")

# print(s2.name, s2.roll_no)  # Zoya 104 ✅

class Employee:
    Employee_count =0
    def __init__(self, name, position , salary):
        self.name = name
        self.positon= position
        self.salary = salary
        Employee.Employee_count += 1
    @classmethod
    def from_string(cls, emp_str):
        name, position, salary = emp_str.split(",")
        return cls(name, position, int(salary))
    @classmethod
    def reset_employee_count(cls):
        cls.Employee_count = 0
    def display_info(self):
        print(f"Name: {self.name}, Position: {self.positon}, Salary: ₹{self.salary}")
# Create employee objects using normal constructor
emp1 = Employee("Mustafa", "Python Developer", 80000)
emp2 = Employee("Aaliyah", "ML Engineer", 95000)
# Create employee object using class method
emp3 = Employee.from_string("Zoya,Data Scientist,90000")
# Display information
emp1.display_info()
emp2.display_info()
emp3.display_info()
# Display employee count
print(f"Total Employees: {Employee.Employee_count}")
# Reset employee count
Employee.reset_employee_count()
print(f"Employee count after reset: {Employee.Employee_count}")
