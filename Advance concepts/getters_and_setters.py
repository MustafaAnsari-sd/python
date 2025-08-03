'''
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks  # private attribute (double underscore)

    # Getter method
    def get_marks(self):
        return self.__marks

    # Setter method
    def set_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
        else:
            print("Invalid marks! Must be between 0 and 100.")

s1 = Student("Alice", 95)
print(s1.get_marks())     # ✅ safe access

s1.set_marks(105)         # ❌ invalid
print(s1.get_marks())     # still 95

s1.set_marks(87)          # ✅ valid
print(s1.get_marks())     # 87
'''

class Temperature:
    def __init__(self, celsius=0):
        self.__celsius = None  # temp default
        self.celsius = celsius  # use setter validation

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        if isinstance(value, (int, float)):
            if value >= -273.15:
                self.__celsius = value
            else:
                print("❌ Temperature can't go below -273.15°C!")
        else:
            print("❌ Celsius must be a number!")

    def to_fahrenheit(self):
        return (self.__celsius * 9/5) + 32


# ✅ Example usage
t = Temperature()
t.celsius = 25
print(t.celsius)         # 25
print(t.to_fahrenheit()) # 77.0
t.celsius = -300         # ❌ Invalid
